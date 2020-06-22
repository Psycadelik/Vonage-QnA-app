import os
from flask import Flask, request, jsonify
from vonage.config import configs


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

    """ This url receives a message using the vonage 2-way sms API and processes it with a reply """
    """ This is where the game logic should reside """

    @app.route("/update/", methods=['POST'])
    def update_url():
        pass

    from . import db
    db.init_app(app)
    return app
