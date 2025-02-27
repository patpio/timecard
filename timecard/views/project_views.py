from flask import Blueprint, render_template, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy import desc
from werkzeug.utils import redirect

from timecard import db
from ..models import Project, Drawing
from ..forms import NewProjectForm, UpdateProjectForm, DeleteProjectForm, AddDrawingForm

bp_project = Blueprint('project', __name__, url_prefix='/projects')


@bp_project.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = NewProjectForm()
    if form.validate_on_submit():
        my_project = Project(user=current_user)
        form.populate_obj(my_project)
        db.session.add(my_project)
        db.session.commit()
        flash(f'Project {my_project.name} has been successfully added.', 'success')
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
    project_form = UpdateProjectForm(obj=my_project)

    if project_form.validate_on_submit():
        project_form.populate_obj(my_project)
        db.session.commit()

        flash(f'Project {my_project.name} has been successfully updated.', 'success')
        return redirect(url_for('project.project', name=my_project.name))

    drawing_form = AddDrawingForm()

    if drawing_form.validate_on_submit():
        drawing = Drawing(project=my_project)
        drawing_form.populate_obj(drawing)
        db.session.add(drawing)
        db.session.commit()

        flash(f'Drawing {drawing.name} has been successfully added.', 'success')
        return redirect(request.referrer)

    return render_template('update.html', project_form=project_form, drawing_form=drawing_form)


@bp_project.route('/delete/<int:project_id>', methods=['POST'])
@login_required
def delete(project_id):
    my_project = Project.query.filter_by(id=project_id)
    my_project.delete()
    db.session.commit()
    flash('Project has been successfully deleted', 'success')
    return redirect(url_for('main.home'))


@bp_project.route('/search')
@login_required
def search():
    if Project.query.filter_by(name=request.args.get('search')).first():
        return redirect(url_for('project.project', name=request.args.get('search')))
    flash('Project not found', 'danger')
    return redirect(request.referrer)
