from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    timecard = Flask(__name__)

    timecard.config.from_object('timecard.config.DevelopmentConfig')

    from .views import bp_main
    from .views import bp_project
    from .views import bp_user

    timecard.register_blueprint(bp_main)
    timecard.register_blueprint(bp_project)
    timecard.register_blueprint(bp_user)

    db.init_app(timecard)
    Migrate(timecard, db)

    return timecard
