from functools import wraps
import jwt
import os
import logging
from flask import request

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

def role_required(list_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            flask_request = request
            # flask_request = args[0] if args else None  # Check if args exists and has elements, Assuming request is the first argument if it exists
            # token = request.headers.get('Authorization') if request else None
            # flask_request = args[0]  # Assuming request is the first argument
            # if flask_request:
            token = flask_request.headers.get('Authorization')
            if not token:
                return {"error": "Token is not valid"}, 401

            try:
                decoded_token = decode_jwt(token)
                print("Decoded Token:", decoded_token)  # Add this line to print the decoded token
                user_role = decoded_token.get("role")
                print("Allowed roles:", list_roles)  # Add this line for debugging
                print("Passed roles:", user_role) 
                # if user_role and any(role.value == user_role for role in list_roles):
                # if user_role and user_role in list_roles:
                # if any(role in user_role for role in list_roles):
                if user_role and user_role.lower() in [role.lower() for role in list_roles]:
                    return fn(*args, **kwargs)
                else:
                    return {"error": f"{list_roles[0].capitalize()} access is required"}, 403
            except jwt.ExpiredSignatureError as e:
                logging.error(f"Expired token error: {e}")
                return {"error": "Token has expired"}, 401
            except jwt.InvalidTokenError as e:
                logging.error(f"Expired token error: {e}")
                return {"error": "Token is not valid"}, 401
            # else:
            #     return {"error": "Request object not found"}, 500  # Adjust the error response as needed
        return wrapper
    return decorator

# def broker_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         # request = args[0] if args else None  # Assuming request is the first argument if it exists
#         # token = request.headers.get('Authorization') if request else None
#         flask_request = args[0]  # Assuming request is the first argument
#         token = flask_request.headers.get('Authorization')
#         if not token:
#             return {"error": "Token is not valid"}, 401

#         try:
#             decoded_token = decode_jwt(token)
#             user_id = decoded_token.get("_id")
#             user_role = decoded_token.get("role")
#             if user_role == ListRole.BROKER.value:
#                 return fn(user_id, user_role, *args, **kwargs)
#             else:
#                 return {"error": "Broker access is required"}, 403
#         except jwt.ExpiredSignatureError:
#             return {"error": "Token has expired"}, 401
#         except jwt.InvalidTokenError:
#             return {"error": "Token is not valid"}, 401
#     return wrapper

# def client_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         # request = args[0] if args else None  # Assuming request is the first argument if it exists
#         # token = request.headers.get('Authorization') if request else None
#         flask_request = args[0]  # Assuming request is the first argument
#         # flask_request = request  # Using the Flask request object directly
#         token = flask_request.headers.get('Authorization')
#         if not token:
#             return {"error": "Token is not valid"}, 401

#         try:
#             decoded_token = decode_jwt(token)
#             user_id = decoded_token.get("_id")
#             user_role = decoded_token.get("role")
#             if user_role == ListRole.CLIENT.value:
#                 return fn(user_id, user_role, *args, **kwargs)
#             else:
#                 return {"error": "Client access is required"}, 403
#         except jwt.ExpiredSignatureError:
#             return {"error": "Token has expired"}, 401
#         except jwt.InvalidTokenError:
#             return {"error": "Token is not valid"}, 401
#     return wrapper

# from functools import wraps
# import jwt, os
# from flask import request # , g
# from user.constants import ListRole

# def decode_jwt(token):
#     try:

#         token = token.replace('Bearer ', '')

#         payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
#         return payload
#     except jwt.ExpiredSignatureError:
#         print("Expired signature error")
#         return None
#     except jwt.InvalidTokenError:
#         print("Invalid token error")
#         return None

# def role_required(list_roles):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             token = request.headers.get('Authorization')
#             if not token:
#                 return {"error": "Token is not valid"}, 401
            
#             try:
#                 decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
#                 user_role = decoded_token.get("role")
#                 if user_role in list_roles: # change '== UserRole.BROKER.value:' into in list_roles
#                     return fn(*args, **kwargs)
#                 else:
#                     return {"error": f"{list_roles[0].capitalize()} access is required"}, 403
#             except jwt.ExpiredSignatureError:
#                 return {"error": "Token has expired"}, 401
#             except jwt.InvalidTokenError:
#                 return {"error": "Token is not valid"}, 401
#         return wrapper
#     return decorator

# def broker_required(fn): # add param , list_roles after fn if there are roles
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         try:
#             token = request.headers.get('Authorization')
#             if not token:
#                 return {"error": "Token is not valid"}, 401
        
#             decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
#             user_id = decoded_token.get("_id")
#             user_role = decoded_token.get("role")
#             if user_role == ListRole.BROKER.value: #change 'in list_role:' into == ListRole.BROKER.value:
#                 return fn(user_id, user_role, *args, **kwargs) #  add user_role
#             else:
#                 return {"error": "Broker access is required"}, 403
#         except jwt.ExpiredSignatureError:
#             return {"error": "Token has expired"}, 401
#         except jwt.InvalidTokenError:
#             return {"error": "Token is not valid"}, 401
#     return wrapper

# def client_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         try:
#             token = request.headers.get('Authorization')
#             if not token:
#                 return {"error": "Token is not valid"}, 401
#             decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms="HS256")
#             user_id = decoded_token.get("_id")
#             user_role = decoded_token.get("role")
#             if user_role == ListRole.CLIENT.value:
#                 return fn(user_id, user_role, *args, **kwargs)
#             else:
#                 return {"error": "Client access is required"}, 403
#         except jwt.ExpiredSignatureError:
#             return {"error": "Token has expired"}, 401
#         except jwt.InvalidTokenError:
#             return {"error": "Token is not valid"}, 401
#     return wrapper