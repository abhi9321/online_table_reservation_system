# online_table_reservation_system

python3 -m venv venv
source venv/bin/activate

```
flask db stamp head

flask db init
flask db migrate
flask db upgrade
```

export FLASK_ENV=development

guest = User(name='Timon',email='timon@gmail.com',password_hash='123')
db.session.add(guest)