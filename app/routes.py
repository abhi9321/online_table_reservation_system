from flask import jsonify

from app import app
from app.models import Restaurant, RestaurantSchema, Table, User, Reservation


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/v1/get_restaurant/', methods=['GET', 'POST'])
def get_restaurant():
    res = Restaurant.query.all()
    res_schema = RestaurantSchema(many=True)
    output = res_schema.dump(res)

    return jsonify({'res': output})
