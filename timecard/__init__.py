from flask import Flask


def create_app():
    timecard = Flask(__name__)

    from .views import bp_main

    timecard.register_blueprint(bp_main)

    return timecard
