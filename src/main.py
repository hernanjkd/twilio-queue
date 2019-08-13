"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import Queeue
from send_sms import send_msg
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

q = Queeue()

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route("/sms", methods=['GET', 'POST'])
def sms():

    name = request.form['Body']
    number = request.form['From']

    q.enqueue(name, number)

    # Unable to create record: The number  is unverified. Trial accounts cannot send messages to
    # unverified numbers; verify  at twilio.com/user/account/phone-numbers/verified, or purchase a
    # Twilio number to send messages to unverified numbers.
    send_msg(3059511070, 'Hello ' + name + ', you are now on the waiting list.')

    return 'ok', 200


@app.route("/new", methods=['POST'])
def add_person():
    body = request.get_json()

    q.enqueue(body['name'], body['number'])

    send_msg(3059511070, body['name'] + ", you are in queeue, we'll let you know when you are next.")

    return jsonify(q.get_queue()), 200


@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(q.get_queue())

@app.route('/next')
def process():
    person = q.dequeue()

    send_msg(3059511070, person['name'] + ', you are next.')

    return 'ok', 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
