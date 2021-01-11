from flask import Blueprint, render_template
from flask_login import login_required

from ..models import User, Project
from timecard import login_manager

bp_main = Blueprint('main', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/')
@login_required
def home():
    return render_template('index.html')


@bp_main.app_context_processor
def latest_5():
    latest_projects = Project.latest(5)
    return dict(latest_projects=latest_projects)


@bp_main.app_context_processor
def admin():
    return dict(admin=User.query.filter_by(username='admin').first())


@bp_main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
