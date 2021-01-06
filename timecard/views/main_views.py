from flask import Blueprint, render_template

from ..models import User, Project
from timecard import login_manager

bp_main = Blueprint('main', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.app_context_processor
def latest_5():
    latest_projects = Project.latest(5)
    return dict(latest_projects=latest_projects)
