from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, MultipleFileField, SubmitField, FormField, \
    FieldList, SelectField, Form, validators
from wtforms.validators import DataRequired


# class DrawingForm(Form):
#     number = IntegerField('Drawing number')
#     name = StringField('Drawing name')
#     description = TextAreaField('Drawing description')
#     status = SelectField('Drawing status', choices=['Need to draw', 'Working on', 'Done'])


class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    project_number = IntegerField('Project number', validators=[validators.Optional()])
    deadline = DateField('Deadline', validators=[validators.Optional()])
    description = TextAreaField('Description')
    # drawings_list = FieldList(FormField(DrawingForm), min_entries=1)
    # files = MultipleFileField('Add files')


class NewProjectForm(ProjectForm):
    submit = SubmitField('Add')


class UpdateProjectForm(ProjectForm):
    submit = SubmitField('Update')


class DeleteProjectForm(FlaskForm):
    submit = SubmitField('Delete')


class SearchProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Search')
