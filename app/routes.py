from flask import request, jsonify
from app import app
from app.models import Restaurant, RestaurantSchema, Table, User, Reservation
from app.controller import create_reservation

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/v1/get_restaurant/<res_id>', methods=['GET'])
@app.route('/v1/get_restaurant/', methods=['GET'])
def get_restaurant(res_id=None):
    if res_id:
        res = Restaurant.query.filter_by(id=res_id)
    else:
        res = Restaurant.query.all()
    res_schema = RestaurantSchema(many=True)
    output = res_schema.dump(res)
    response = {'status': 'success', 'details': output}
    return jsonify(response)

@app.route('/v1/make_reservation', methods=['GET', 'POST'])
def make_reservation():
    data_set = request.get_json()
    reservation = create_reservation(data_set)
    return jsonify(reservation)


@app.route('/v1/register_user/', methods=['GET', 'POST'])
def register_user():
    data_set = request.get_json()
    print(data_set)
