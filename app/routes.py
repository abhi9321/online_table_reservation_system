from flask import request, jsonify
from app import app
from app.models import Restaurant, RestaurantSchema, Table, User, Reservation


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/v1/get_restaurant/<res_id>', methods=['GET', 'POST'])
@app.route('/v1/get_restaurant/', methods=['GET', 'POST'])
def get_restaurant(res_id=None):
    if res_id:
        res = Restaurant.query.filter_by(id=res_id)
    else:
        res = Restaurant.query.all()
    res_schema = RestaurantSchema(many=True)
    output = res_schema.dump(res)
    response = {'status': 'success', 'details': output}
    return jsonify(response)
