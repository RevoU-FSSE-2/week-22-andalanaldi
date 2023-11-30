from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from db import db
import os

from auth.auth_service import auth_service
from ipotodow.ipo_service import ipo_service

app = Flask(__name__)
CORS(app)

# Configuration to match helmet middleware settings in express js
csp = {
    'default-src': '\'self\'',
    'frame-ancestors': '\'none\'',
    'base-uri': '\'self\'',
    'object-src': '\'none\'',
    'img-src': '*',
}

talisman = Talisman(
    app,
    content_security_policy=csp,
    frame_options='deny',
    hide_powered_by=True,
    force_https=True,  # Equivalent to HSTS in helmet
    force_https_permanent=True,
    referrer_policy='strict-origin-when-cross-origin',
    session_cookie_secure=True,
    session_cookie_http_only=True,
    content_type_nosniff=True,
    feature_policy={
        'geolocation': '\'none\'',
        'midi': '\'none\'',
        'sync-xhr': '\'none\'',
    }
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

app.register_blueprint(auth_service, url_prefix='/auth')
app.register_blueprint(ipo_service, url_prefix='/ipo')


# with app.app_context():
#     db_init()

# pipenv install flask flask-cors V
# pipenv install pymongo X
# pipenv install python-dotenv X
# pipenv install python-jose[cryptography] X
# pipenv install marshmallow V
