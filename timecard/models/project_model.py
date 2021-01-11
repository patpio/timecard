from datetime import date

from sqlalchemy import desc

from timecard import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    project_number = db.Column(db.Integer)
    date_created = db.Column(db.Date, default=date.today())
    deadline = db.Column(db.Date)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    drawings = db.relationship('Drawing', backref='project', lazy='dynamic')
    # files =

    @staticmethod
    def latest(num):
        return Project.query.order_by(desc(Project.id)).limit(num)
