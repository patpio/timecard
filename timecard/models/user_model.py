from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from timecard import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String)
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('Password: write only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return f'<User {self.username}>'
