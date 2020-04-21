from app.models import Restaurant, RestaurantSchema, Table, User, Reservation
from app.mail_util import send_mail
from app import app, db
import datetime
import app

config = app.Config()
DEFAULT_RESERVATION_LENGTH = 1  # 1 hour


def notify(response):
    # print(response['details']['email'])
    message = """ Hi """ + str(response['details']['user_name']) + """,\n\n Reservation confirmed for """ + \
              str(response['details']['reservation_datetime']) + """."""

    data = {'from': config.sender_email_id,
            'sender_email_id_password': config.sender_email_id_password,
            'to': 'agopalaiah@quotient.com',
            'subject': 'Reservation successful',
            'message': message}
    print(data)
    send_mail(**data)


def create_reservation(data):
    response = {'status': 'success'}
    reservation_time = datetime.datetime.strptime(data.get('reservation_datetime'), '%Y-%m-%d %H:%M:%S')
    if datetime.datetime.now() > reservation_time:
        response.update({'status': 'error', 'message': f'cannot book for date {reservation_time}'})
        return response
    user = User.query.filter_by(phone_number=data.get('phone_number')).first()
    if user is None:
        print('user not present')
        user = User(name=data.get('user_name'), phone_number=data.get('phone_number'), email=data.get('email'))
        db.session.add(user)

    # now check table availability
    capacity = int(data.get('num_guest'))
    tables = Table.query.filter(Table.restaurant_id == data.get('restaurant_id'), Table.capacity >= capacity).order_by(
        Table.capacity.asc()).all()

    t_ids = [t.id for t in tables]
    print(f'table ids which has the capacity : {t_ids}')

    if not t_ids:
        # no tables with that size
        print(f'no tables available for the capacity : {capacity}')
        response.update({'status': 'error', 'message': f'no tables available for the capacity : {capacity}'})
        return response

    # check reservations
    begin_range = reservation_time - datetime.timedelta(hours=DEFAULT_RESERVATION_LENGTH)
    end_range = reservation_time + datetime.timedelta(hours=DEFAULT_RESERVATION_LENGTH)

    reservations = Reservation.query.join(Reservation.table).filter(Table.id.in_(t_ids),
                                                                    Reservation.reservation_time >= begin_range,
                                                                    Reservation.reservation_time <= end_range).order_by(
        Table.capacity.desc()).all()

    # Reservation.query.join(Reservation.table).filter(Table.id.in_([2,3])).order_by(Table.capacity.desc()).all()
    print(f'reservations : {reservations}')

    if reservations:
        if len(t_ids) == len(reservations):
            # no available tables, sorry
            # still add guest
            print(f'not available')
            db.session.commit()
            response.update({'status': 'error', 'message': f'tables not available for given time'})
            return response
        else:
            # get available table

            table_id = (set(t_ids) - set([r.table.id for r in reservations])).pop()
            print(f' available table: {table_id}')

            user_id = int(User.query.filter_by(phone_number=data.get('phone_number')).with_entities(User.id).first()[0])
            print(f'user id : {user_id}')

            reservation = Reservation(restaurant_id=data.get('restaurant_id'), table_id=table_id,
                                      user_id=user_id,
                                      num_guests=capacity,
                                      reservation_time=reservation_time)
    else:
        # we are totally open
        user_id = int(User.query.filter_by(phone_number=data.get('phone_number')).with_entities(User.id).first()[0])
        table_id = int(Table.query.filter_by(id=int(t_ids[0]), restaurant_id=data.get('restaurant_id')).with_entities(
            Table.id).first()[0])

        reservation = Reservation(restaurant_id=data.get('restaurant_id'), table_id=table_id,
                                  user_id=user_id,
                                  num_guests=capacity,
                                  reservation_time=reservation_time)

    db.session.add(reservation)
    db.session.commit()

    response.update({'message': f'reservation successful', 'details': data})
    print(response)
    if response['status'] == 'success':
        pass
        # notify(response)
    return response
