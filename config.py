import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # set configs
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    sender_email_id = 'abhishekh@gmail.com'
    sender_email_id_password = 'xxx'
    # receiver_email_id = 'abhishek@gmail.com

