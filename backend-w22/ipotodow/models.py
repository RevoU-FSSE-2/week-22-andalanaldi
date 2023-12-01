from db import db
from datetime import datetime

class ipotodow18(db.Model): # IPO
    _id = db.Column(db.Integer, primary_key=True)
    clientid = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    # clientid = db.Column(db.String(50), nullable=False)
    tickercode = db.Column(db.String(50), nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    outstanding = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # Set default status as 'pending'
    priority = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Foreign key relationship with User
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('users', backref='ipotodow18s')