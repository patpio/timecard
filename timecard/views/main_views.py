from flask import Blueprint, render_template

from ..models import Project

bp_main = Blueprint('main', __name__, url_prefix='/')


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.app_context_processor
def latest_5():
    latest_projects = Project.latest(5)
    return dict(latest_projects=latest_projects)
