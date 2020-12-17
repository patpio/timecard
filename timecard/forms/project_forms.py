from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, MultipleFileField, SubmitField, FormField, \
    FieldList, SelectField, Form
from wtforms.validators import DataRequired


# class DrawingForm(Form):
#     number = IntegerField('Drawing number')
#     name = StringField('Drawing name')
#     description = TextAreaField('Drawing description')
#     status = SelectField('Drawing status', choices=['Need to draw', 'Working on', 'Done'])


class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # project_number = IntegerField('Project number')
    # date_created = DateField('Creation date')
    # deadline = DateField('Deadline')
    # description = TextAreaField('Description')
    # drawings_list = FieldList(FormField(DrawingForm), min_entries=1)
    # files = MultipleFileField('Add files')
    submit = SubmitField('Add')
