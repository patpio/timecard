from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    timecard = Flask(__name__)

    timecard.config.from_object('timecard.config.DevelopmentConfig')

    from .views import bp_main
    from .views import bp_project
    from .views import bp_user
    from .views import bp_auth

    timecard.register_blueprint(bp_main)
    timecard.register_blueprint(bp_project)
    timecard.register_blueprint(bp_user)
    timecard.register_blueprint(bp_auth)

    db.init_app(timecard)
    Migrate(timecard, db)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(timecard)

    return timecard
