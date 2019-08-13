"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import Queeue
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
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


@app.route("/new", methods=['POST'])
def add_person():
    body = request.get_json()

    q.enqueue(body['name'], body['number'])

    return "ok", 200


@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(q)



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
