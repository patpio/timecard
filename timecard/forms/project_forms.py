from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, SubmitField, FormField, \
    FieldList, validators
from wtforms.validators import DataRequired

from .drawing_forms import DrawingForm


class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    project_number = IntegerField('Project number', validators=[validators.Optional()])
    deadline = DateField('Deadline', validators=[validators.Optional()])
    description = TextAreaField('Description')
    # files = MultipleFileField('Add files')


class NewProjectForm(ProjectForm):
    submit = SubmitField('Add')


class UpdateProjectForm(ProjectForm):
    drawings = FieldList(FormField(DrawingForm), min_entries=1)
    submit = SubmitField('Update')


class DeleteProjectForm(FlaskForm):
    submit = SubmitField('Delete')
