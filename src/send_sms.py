# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


def send_msg(number, msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+17544659472',
                        to=number
                    )

    print(message.sid)