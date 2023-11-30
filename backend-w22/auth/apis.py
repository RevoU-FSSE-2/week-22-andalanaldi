from flask import Blueprint, request
from common.bcrypt import bcrypt
import bcrypt
from user.models import User
from db import db
import jwt, os
from datetime import datetime, timedelta
from marshmallow import Schema, fields, ValidationError, validate
import re

auth_service = Blueprint("auth", __name__)

# Custom validator function for password
def validate_password(password):
    if not re.match(r'^(?=.*\d)(?=.*[a-zA-Z]).{8,100}$', password):
        raise ValidationError('Password must be between 8 and 100 characters and contain both letters and numbers')

# Marshmallow schema for request validation
class UserRegistrationSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, validate=validate_password)
    role = fields.Str(required=True, validate=validate.OneOf(['client', 'broker']))


# Register endpoint
@auth_service.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    schema = UserRegistrationSchema()

    try:
        data = schema.load(data)
    except ValidationError as err:
        return {"success": False, "message": err.messages}, 400
    # "error": err.messages

    if 'password' not in data:
        return {"success": False, "message": "Password is required"}, 400

    if not re.match(r'^(?=.*\d)(?=.*[a-zA-Z]).{8,100}$', data['password']):
        return {"success": False, "message": "Password must be between 8 and 100 characters and contain both letters and numbers"}, 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = User(
        username=data['username'], 
        password=hashed_password,
        role=data['role'] # Set the role for the new user
    )
    
    db.session.add(new_user)
    db.session.commit()

    return {
        'user_id': new_user.user_id,
        'username': new_user.username,
        'role': new_user.role  # Return the role in the response  
        # "success" : True,
        # "message": "Successfully register a user",
        # "data": new_user.id      
    }

# Login endpoint
@auth_service.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if not username or not password:
        return ({"error": "Username or password is missing"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return {"error": "Username or password is not valid"}, 401
    
    valid_password = bcrypt.check_password_hash(user.password, password)
    if not valid_password:
        return {"error": "Username or password is not valid"}, 401
    
    payload = {
        'user_id': user.user_id,
        'username': user.username,
        'role': user.role.value,
        'exp': datetime.utcnow() + timedelta(minutes=30) # extend token expiration from 1 to 30 minutes to help debugging
    }
    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm="HS256")
    
    return {
        'token': token
        # 'success': True,
        # 'message': 'Successfully login',
        # 'data': {
        #     'token': token,
        #     'username': user.username,
        #     'email': user.email,
        #     'id': user.id,
        #     'role': user.role.value
        # }
    }


# Logout endpoint
@auth_service.route('/logout', methods=['POST'])
def logout():
    # Implement your logout logic here
    return {'message': 'Logout functionality'}, 200