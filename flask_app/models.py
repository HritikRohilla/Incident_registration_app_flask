from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    incidents = db.relationship('Incident', backref='user', lazy=True)

class Incident(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    incident_type = db.Column(db.String(50), nullable=False)
    reporter_name = db.Column(db.String(50), nullable=False)
    incident_details = db.Column(db.Text, nullable=False)
    reported_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    priority = db.Column(db.String(10), nullable=False)
    incident_status = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)