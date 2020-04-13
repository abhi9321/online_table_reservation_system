import datetime

from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(120))
    address = db.Column(db.String(225))
    amount_per_person = db.Column(db.Integer)

    def __repr__(self):
        return '<name {}>'.format(self.name)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    capacity = db.Column(db.Integer)

    def __repr__(self):
        return '<Table id {}>'.format(self.id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    check_in = db.Column(db.DateTime, index=True, default=datetime)

    def __repr__(self):
        return '<Reservation {}>'.format(self.id)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.String(120), index=True, unique=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return '<dish {}>'.format(self.dish)
