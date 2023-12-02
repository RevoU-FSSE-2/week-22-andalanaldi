from firebase_functions import https_fn
import os
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from common.bcrypt import bcrypt
from db import db, db_init


from auth.apis import auth_service
from ipotodow.apis import ipo_service

app = Flask(__name__)
CORS(app)
Talisman(app)

# # Configuration to match helmet middleware settings in express js SELF = "'self'"
# csp = {
#     'default-src': '\'self\'',
#     'frame-ancestors': '\'none\'',
#     'base-uri': '\'self\'',
#     'object-src': '\'none\'',
#     'img-src': '*',
# }

# talisman = Talisman(
#     app,
#     content_security_policy=csp,
#     frame_options='deny',
#     content_security_policy_nonce_in=['script-src','style-src'],
#     hide_powered_by=True, #
#     force_https=True,  # Equivalent to HSTS in helmet
#     force_https_permanent=True,
#     referrer_policy='strict-origin-when-cross-origin',
#     session_cookie_secure=True,
#     session_cookie_http_only=True,
#     content_type_nosniff=True, #
#     feature_policy={
#         'geolocation': '\'none\'',
#         'midi': '\'none\'',
#         'sync-xhr': '\'none\'',
#     }
# )

database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_service, url_prefix='/auth')
app.register_blueprint(ipo_service, url_prefix='/ipo')


# with app.app_context():
#     db_init()

@app.route('/health-check', methods=['POST'])
def generate_article():
    return "Server OK"

# nama function nya articles, ini bisa diganti dengan id atau nama student
# nama ini untuk integrasi flask ke cloud function
@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()

# pipenv install flask flask-cors V
# pipenv install pymongo X
# pipenv install python-dotenv X
# pipenv install python-jose[cryptography] X
# pipenv install marshmallow V
