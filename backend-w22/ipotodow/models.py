from db import db
from datetime import datetime

class IPO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientid = db.Column(db.String(50), nullable=False)
    tickercode = db.Column(db.String(50), nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    outstanding = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
