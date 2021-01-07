from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Your username: ', validators=[DataRequired()])
    password = PasswordField('Your password: ', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = StringField('Your username: ', validators=[DataRequired(), Length(3, 40)])
    email = StringField('Your email: ', validators=[DataRequired(), Length(3, 80), Email()])
    password = PasswordField('Your password: ',
                             validators=[DataRequired(), EqualTo('confirm_password', message='Password must match.')])
    confirm_password = PasswordField('Repeat your password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    @staticmethod
    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('Username already exist.')

    @staticmethod
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('Email already taken.')
