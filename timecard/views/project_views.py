from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from ..forms import ProjectForm

bp_project = Blueprint('projects', __name__, url_prefix='/projects')


@bp_project.route('/add', methods=['GET', 'POST'])
def add():
    form = ProjectForm()
    if form.validate_on_submit():
        print('Successfully added')
        return redirect(url_for('main.home'))

    return render_template('add.html', form=form)


@bp_project.route('/projects')
def projects():
    return render_template('projects.html')


@bp_project.route('/<name>')
def project():
    return render_template('project.html')
