from db import db

# Tabel User
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False) 
    # Ensure this line above aligns with the password length constraint between the password validation constraint and the database column length
    role = db.Column(db.String(20), nullable=False, default='client')
    