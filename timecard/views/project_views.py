from flask import Blueprint, render_template, url_for, flash, request
from flask_login import login_required
from sqlalchemy import desc
from werkzeug.utils import redirect

from timecard import db
from ..models import Project
from ..forms import NewProjectForm, UpdateProjectForm, DeleteProjectForm, SearchProjectForm

bp_project = Blueprint('project', __name__, url_prefix='/projects')


@bp_project.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = NewProjectForm()
    if form.validate_on_submit():
        my_project = Project()
        form.populate_obj(my_project)
        db.session.add(my_project)
        db.session.commit()
        flash(f'Project {my_project.name} has been successfully added', 'success')
        return redirect(url_for('project.project', name=my_project.name))

    return render_template('add.html', form=form)


@bp_project.route('/projects')
@login_required
def projects():
    my_projects = Project.query.order_by(desc(Project.id))
    return render_template('projects.html', projects=my_projects)


@bp_project.route('/<name>')
@login_required
def project(name):
    my_project = Project.query.filter_by(name=name).first_or_404()
    delete_form = DeleteProjectForm()
    return render_template('project.html', project=my_project, delete_form=delete_form)


@bp_project.route('/update/<int:project_id>', methods=['GET', 'POST'])
@login_required
def update(project_id):
    my_project = Project.query.filter_by(id=project_id).first_or_404()
    form = UpdateProjectForm(obj=my_project)

    if form.validate_on_submit():
        form.populate_obj(my_project)
        db.session.commit()

        flash(f'Project {my_project.name} has been successfully updated', 'success')
        return redirect(url_for('project.project', name=my_project.name))

    return render_template('update.html', form=form)


@bp_project.route('/delete/<int:project_id>', methods=['POST'])
@login_required
def delete(project_id):
    my_project = Project.query.filter_by(id=project_id)
    my_project.delete()
    db.session.commit()
    flash('Project has been successfully deleted', 'success')
    return redirect(url_for('main.home'))


@bp_project.route('/search', methods=['POST'])
@login_required
def search():
    form = SearchProjectForm()
    project = Project.query.filter_by(name=form.name.data).first_or_404()
    return redirect(url_for('project.project', name=project.name))
