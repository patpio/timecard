from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from timecard import db
from ..models import Project
from ..forms import ProjectForm

bp_project = Blueprint('projects', __name__, url_prefix='/projects')


@bp_project.route('/add', methods=['GET', 'POST'])
def add():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('add.html', form=form)


# @bp_project.route('/projects')
# def projects():
#     # projects = Project.query.all()
#     return render_template('projects.html', projects=projects)
#
#
# @bp_project.route('/<name>')
# def project(name):
#     # project = Project.query.filter_by(name=name).first_or_404()
#     return render_template('project.html', project=project)
