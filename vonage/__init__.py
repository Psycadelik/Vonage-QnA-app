import os
import sys


from flask import Flask, request, jsonify
from vonage.config import configs
from vonage.nexmo import nexmo_sms
from dialogflowapi.intent_texts import detect_intent_texts
from two_way_sms_api.send_sms import send_sms


def create_app(environment='development', test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs[environment])
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'vonage.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=['GET'])
    def landing_url():
        res = "welcome to the Vonage QnA landing page"
        return res

    """ this url defines the behaviour when a new call is taking place """

    @app.route("/inbound/", methods=['POST'])
    def inbound_sms():
        pass

    @app.route("/status/", methods=['POST'])
    def status_url():
        pass

    """ This url receives RTC events dispatched by the conversation API """

    @app.route("/event/", methods=['GET'])
    def event_url():
        pass

    """ The notify URL is the entry point to the QnA game. Users opt in by choosing either 1(geographical questions),
    2(Historical questions),3a(Music), 3b (Games), 3c (Movies)  or 4 (Exit)"""

    @app.route("/webhooks/notify/", methods=['POST'])
    def notify_url():
        number = request.get_json().get('number')
        notification = "Hello. You can start your quiz with quizzie-bot by sending the following keywords: hi," \
                       " hello or vonage."

        return nexmo_sms(notification, number)

    """ This url receives a message using the vonage 2-way sms API and processes it with a reply """
    """ This is where the game logic should reside """

    @app.route("/webhooks/update/", methods=['POST'])
    def update_url():
        trigger = request.get_json().get('message')
        project_id = os.getenv("PROJECT_ID")
        session_id = os.getenv("SESSION_ID")
        language_code = os.getenv("LANG_CODE")

        response = detect_intent_texts(project_id, session_id, trigger, language_code)
        number = open("phone_numbers.txt", 'r')
        phone = number.readlines()[0]

        return send_sms(response, phone)

    from . import db
    db.init_app(app)
    return app
