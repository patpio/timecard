from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SelectField, SubmitField


class DrawingForm(FlaskForm):
    number = IntegerField('Drawing number')
    name = StringField('Drawing name')
    description = TextAreaField('Drawing description')
    status = SelectField('Drawing status', coerce=int, choices=[(1, 'Need to draw'), (2, 'Working on'), (3, 'Done')])


class AddDrawingForm(DrawingForm):
    submit = SubmitField('Add')
