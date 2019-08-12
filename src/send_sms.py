# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6d10ad13c49fca9e8637121ac1c35611'
auth_token = '18a2e01333efc96d888907598ce2142d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17544659472',
                     to='+13059511070'
                 )

print(message.sid)