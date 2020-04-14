import datetime

from app import db, ma

DEFAULT_RESERVATION_LENGTH = 1  # 1 hour


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(120))
    address = db.Column(db.String(225))
    amount_per_person = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id}, {self.name}'


class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'address', 'amount_per_person')
        # model = Restaurant


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    capacity = db.Column(db.Integer)

    def __repr__(self):
        return '<Table id {}>'.format(self.id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship('Restaurant')
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    table = db.relationship('Table')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    num_guests = db.Column(db.Integer, index=True)
    reservation_time = db.Column(db.DateTime, index=True, default=datetime)

    def __repr__(self):
        return '<Reservation {}>'.format(self.id)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.String(120), index=True, unique=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return '<dish {}>'.format(self.dish)


class MenuSchema(ma.Schema):
    class Meta:
        fields = ('id', 'dish', 'cost')
