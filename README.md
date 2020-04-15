# online_table_reservation_system

online table reservation system project:
- allows user to check for various restaurants
- book available tables 
- provides options to get the menu list. 

```
python3 -m venv venv
source venv/bin/activate
export FLASK_ENV=development
flask run
or 
run  -> run.py

```
```
db migration
flask db stamp head
flask db init
flask db migrate
flask db upgrade
```

API:
---
- get restaurants:
```
curl --location --request GET 'http://127.0.0.1:5000/v1/get_restaurant/1' \
--header 'Content-Type: application/json' \
--data-raw '{"user_name":"abhishek","phone_number":"9912345678","num_guest":"4","restaurant_id":"1","reservation_datetime": "2020-04-15 05:00:00"}'
```

- update reservation
```
curl --location --request POST 'http://127.0.0.1:5000/v1/make_reservation' \
--header 'Content-Type: application/json' \
--data-raw '{"user_name":"abhishek","phone_number":"9912345678","email":"abhishek@gmail.com","num_guest":"4","restaurant_id":"1","reservation_datetime": "2020-04-16 03:00:00"}'
```

- get menu
```
curl --location --request GET 'http://127.0.0.1:5000/v1/get_menu/1' \
--header 'Content-Type: application/json' \
--data-raw '{"user_name":"abhishek","phone_number":"9912345678","num_guest":"4","restaurant_id":"1","reservation_datetime": "2020-04-15 05:00:00"}'
```