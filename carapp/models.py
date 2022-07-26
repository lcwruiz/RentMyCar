import logging as lg
from posixpath import supports_unicode_filenames
from unicodedata import name

from flask_sqlalchemy import SQLAlchemy

from .views import app

db = SQLAlchemy(app)

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Vehicule("Audi", "A3 Sportback"))
    db.session.add(Vehicule("Mercedes", "AMG-GT"))
    db.session.commit()
    lg.warning('Database initialized!')


class Vehicule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)

    def __init__(self, brand, model, is_available):
        self.brand = brand
        self.model = model
        self.is_available = is_available
        
class User(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.relationship('User', backref='id', lazy=True)
    
    def __init__(self, user_id):
        self.user_id = user_id


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.relationship('Customer', backref='id', lazy=True)
    car_id = db.relationship('Vehicule', backref='id', lazy=True)

    def __init__(self, customer_id, car_id):
        self.customer_id = customer_id
        self.car_id = car_id
        
    
    
db.create_all()