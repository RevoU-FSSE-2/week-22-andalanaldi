from functools import wraps
import jwt, os
from flask import request
# , g
from user.constants import ListRole

def decode_jwt(token):
    try:

        token = token.replace('Bearer ', '')

        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("Expired signature error")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token error")
        return None

def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return {"error": "Token is not valid"}, 401
            
            try:
                decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
                user_role = decoded_token.get("role")
                if user_role in roles: # change '== UserRole.BROKER.value:' into in list_roles
                    return fn(*args, **kwargs)
                else:
                    return {"error": f"{roles[0].capitalize()} access is required"}, 403
            except jwt.ExpiredSignatureError:
                return {"error": "Token has expired"}, 401
            except jwt.InvalidTokenError:
                return {"error": "Token is not valid"}, 401
        return wrapper
    return decorator

def broker_required(fn): # add param , list_roles after fn if there are roles
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {"error": "Token is not valid"}, 401
        
        try:
            decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
            user_id = decoded_token.get("user_id")
            user_role = decoded_token.get("role")
            if user_role == ListRole.BROKER.value: #change 'in list_role:' into == ListRole.BROKER.value:
                return fn(user_id, user_role, *args, **kwargs) #  add user_role
            else:
                return {"error": "Broker access is required"}, 403
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Token is not valid"}, 401
    return wrapper

def client_required(fn): # add param , list_roles after fn if there are roles
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {"error": "Token is not valid"}, 401
        
        try:
            decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
            user_id = decoded_token.get("user_id")
            user_role = decoded_token.get("role")
            if user_role == ListRole.CLIENT.value: #change 'in list_role:' into == ListRole.BROKER.value:
                return fn(user_id, user_role, *args, **kwargs) #  add user_role
            else:
                return {"error": "Client access is required"}, 403
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Token is not valid"}, 401
    return wrapper