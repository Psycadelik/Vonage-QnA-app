import os
from flask import Flask, request, jsonify
from vonage.config import configs
from vonage.nexmo import nexmo_sms
from quiz.geography_quiz import geography_quiz, history_quiz, music_quiz, gaming_quiz, movies_quiz


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

    @app.route("/notify/", methods=['POST'])
    def notify_url():
        number = request.get_json().get('number')
        notification = "Welcome to the Vonage QnA quiz app. Opt in by replying with either: 1 (Geographical Quiz)," \
                       "2 (History quiz), 3a (Music quiz), 3b (Gaming quiz), 3c (Movies quiz) " \
                       "or 4 to Exit"

        return nexmo_sms(notification, number)

    """ This url receives a message using the vonage 2-way sms API and processes it with a reply """
    """ This is where the game logic should reside """

    @app.route("/update/", methods=['POST'])
    def update_url():
        trigger = request.get_json().get('message')
        if trigger == '1':
            geography_quiz(trigger)

        elif trigger == '2':
            history_quiz(trigger)

        elif trigger == '3a':
            music_quiz(trigger)

        elif trigger == '3b':
            gaming_quiz(trigger)

        elif trigger == '3c':
            movies_quiz(trigger)

        elif trigger == '4':
            res = jsonify("Thank you for trying us out. Try again some time")
            return res
        else:
            return jsonify("Failed. Please start with sending play.")

    from . import db
    db.init_app(app)
    return app
