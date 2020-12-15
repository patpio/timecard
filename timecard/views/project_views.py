from flask import Blueprint, render_template

bp_project = Blueprint('projects', __name__, url_prefix='/projects')


@bp_project.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('add.html')


@bp_project.route('/projects')
def projects():
    return render_template('projects.html')
