from flask import Blueprint, request
from marshmallow import Schema, fields, validate, ValidationError
from ipotodow.models import IPO
from auth.utils import role_required, broker_required, client_required
from user.constants import ListRole
from db import db

ipo_service = Blueprint("ipo_service", __name__)

# Marshmallow schema for request validation
class IPOSchema(Schema):
    clientid = fields.String(required=True)
    tickercode = fields.String(required=True)
    purpose = fields.String(required=True)
    outstanding = fields.Float(required=True)
    status = fields.String(required=True, validate=validate.OneOf(['approved', 'rejected']))
    priority = fields.Integer(required=True)
    deadline = fields.DateTime(required=True)

# Marshmallow schema for request validation - for PUT method
class IPOUpdateSchema(Schema):
    tickercode = fields.String(required=False)
    purpose = fields.String(required=False)
    outstanding = fields.Float(required=False)
    priority = fields.Integer(required=False)

# Marshmallow schema for request validation - for PUT method by Broker
class IPOBrokerUpdateSchema(Schema):
    status = fields.String(required=True, validate=validate.OneOf(['approved', 'rejected']))


# Get all IPOs
@ipo_service.route('/', methods=['GET'])
@role_required([ListRole.CLIENT.value, ListRole.BROKER.value])
@client_required(["client","broker"])
def get_all_ipo_to_do():
    role = request.args.get('role')
    user_id = request.args.get('id')

    try:
        if role == 'client':
            ipo = IPO.query.filter_by(clientid=user_id).all()
        else:
            ipo = IPO.query.all()

        ipo_data = [{
            "clientid": item.clientid, 
            "tickercode": item.tickercode, 
            "purpose": item.purpose,
            "outstanding": item.outstanding, 
            "status": item.status, 
            "priority": item.priority,
            "deadline": item.deadline.strftime('%Y-%m-%d %H:%M:%S')} for item in ipo]

        return {
            'message': 'To Do List of IPO Order Preparations successfully retrieved', 
            'data': ipo_data
            }, 200

    except Exception as e:
        return {'error': str(e)}, 500

# Create IPO
@ipo_service.route('/new', methods=['POST'])
# def function untuk cek role
@client_required(["client"])
def create_ipo_to_do():
    try:
        data = request.json
        # ipo = IPOSchema().load(data)
        ipo_schema = IPOSchema()

        # Validate and deserialize data
        errors = ipo_schema.validate(data)
        if errors:
            return {'error': errors}, 400

        # Remove validation fields before creating the IPO object
        validated_data = ipo_schema.load(data)

        new_ipo = IPO(**validated_data)
        # **ipo
        db.session.add(new_ipo)
        db.session.commit()

        return {
            'message': 'To Do List of IPO Order Preparations successfully created',
            'data': {'id': new_ipo.id}
            }, 200

    except ValidationError as e:
        return {'error': e.messages}, 400
    except Exception as e:
        return {'error': str(e)}, 500

# Update IPO
@ipo_service.route('/update/<int:ipo_id>', methods=['PUT'])
@client_required(["client"])
def update_ipo_to_do(ipo_id):
    try:
        data = request.json
        # ipo = IPOSchema().load(data)
        ipo_update_schema = IPOUpdateSchema()

        # updated_ipo 
        # Validate and deserialize data for update
        ipo_update = ipo_update_schema.load(data)

        ipo_record = IPO.query.filter_by(id=ipo_id).first()
        # .update(ipo)

        if ipo_record:
            for attr, value in ipo_update.items():
                if value is not None:
                    setattr(ipo_record, attr, value)

            db.session.commit()
            return {'message': 'To Do List of IPO Order Preparations updated successfully'}, 200
        else:
            return {'error': 'To Do List of IPO Order Preparations not found'}, 404

        # if updated_ipo == 0:
        #     return {'error': 'To Do List of IPO Order Preparations not found'}, 404

        # return {'message': 'To Do List of IPO Order Preparations updated successfully'}, 200

    except ValidationError as e:
        return {'error': e.messages}, 400
    except Exception as e:
        return {'error': str(e)}, 500

# Delete IPO
@ipo_service.route('/delete/<int:ipo_id>', methods=['DELETE'])
@client_required(["client"])
def delete_ipo_to_do(ipo_id):
    try:
        ipo = IPO.query.filter_by(id=ipo_id).first()

        if ipo:
            # Check user's role and ID before deletion
            # if ipo.user_id != current_user.user_id:
            #     return {'error': 'Forbidden Access'}, 403

            db.session.delete(ipo)
            db.session.commit()

            return {'message': 'To Do List of IPO Order Preparations deleted successfully'}, 200
        else:
            return {'error': 'To Do List of IPO Order Preparations not found'}, 404

    # try:
    #     deleted_ipo = IPO.query.filter_by(id=ipo_id).delete()
    #     db.session.commit()

    #     if deleted_ipo == 0:
    #         return {'error': 'To Do List of IPO Order Preparations not found'}, 404

    #     return {'message': 'To Do List of IPO Order Preparations deleted successfully'}, 200
    except Exception as e:
        return {'error': str(e)}, 500

# additional notes for checking current user login
# pip install flask-login
# from flask import Flask
# from flask_login import LoginManager

# app = Flask(__name__)
# login_manager = LoginManager(app)

# @login_manager.user_loader
# def load_user(user_id):
#     # Implement a function to load the user from your database based on user_id
#     # Example: return User.query.get(int(user_id))
#     pass

# from flask_login import login_user, current_user

# # Example login route
# @app.route('/login', methods=['POST'])
# def login():
#     # Authenticate the user and retrieve the user object
#     # Example: user = User.query.filter_by(username=form.username.data).first()

#     # Once authenticated, log in the user
#     # Example: login_user(user)
#     pass


# Approval IPO
@ipo_service.route('/approval/<int:ipo_id>', methods=['PUT'])
@broker_required(["broker"])
def approval_ipo(ipo_id): # add (user_id, user_role) from auth utils.py
    try:
        data = request.json
        ipo = IPOBrokerUpdateSchema().load(data)
        # (only=['status'])
        ipo_record = IPO.query.filter_by(id=ipo_id).first()

        if ipo_record:
            ipo_record.status = ipo.get('status')
            db.session.commit()

            return {'message': 'To Do List of IPO Order Preparations status successfully updated'}, 200
        else:
            return {'error': 'To Do List of IPO Order Preparations not found'}, 404
        # updated_ipo = IPO.query.filter_by(id=ipo_id).update(ipo)
        # db.session.commit()

        # if updated_ipo == 0:
        #     return {'error': 'To Do List of IPO Order Preparations not found'}, 404

        # return {'message': 'To Do List of IPO Order Preparations status successfully updated'}, 200

    except ValidationError as e:
        return {'error': e.messages}, 400
    except Exception as e:
        return {'error': str(e)}, 500
