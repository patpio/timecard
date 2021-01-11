from wtforms import Form, IntegerField, StringField, TextAreaField, SelectField


class DrawingForm(Form):
    number = IntegerField('Drawing number')
    name = StringField('Drawing name')
    description = TextAreaField('Drawing description')
    status = SelectField('Drawing status', choices=['Need to draw', 'Working on', 'Done'])
