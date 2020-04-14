"""
input :
    data = {'from': sender_email_id,
            'sender_email_id_password': sender_email_id_password,
            'to': receiver_email_id,
            'subject': 'Alert',
            'message': 'This is a test msg'
            }
    send_mail(**data)
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(**kwargs):
    # creates SMTP session
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    # Identify yourself to an ESMTP server using EHLO
    s.ehlo()
    # start TLS Transport Layer Security for security
    s.starttls()

    s.login(kwargs['from'], kwargs['sender_email_id_password'])

    msg = MIMEMultipart()
    message = kwargs['message']
    msg['From'] = kwargs['from']
    msg['To'] = kwargs['to']
    msg['CC'] = ''
    msg['Subject'] = kwargs['subject']

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # send the message via the server set up earlier.
    s.sendmail(msg['From'], msg['To'], str(msg))
    print('Mail Successfully sent to ', msg['To'])

    # Terminate the SMTP session and close the connection
    s.close()
