from flask import Flask, render_template, request, redirect, url_for
from flask_app import create_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hritik_rohilla:Qwerty@localhost/postgres'
db = SQLAlchemy(app)

# Define User and Incident models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pin_code = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

class Incident(db.Model):
    id = db.Column(db.String(15), primary_key=True)
    enterprise_or_govt = db.Column(db.String(50), nullable=False)
    reporter_name = db.Column(db.String(50), nullable=False)
    incident_details = db.Column(db.Text, nullable=False)
    reported_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    priority = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database
db.create_all()

