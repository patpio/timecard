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
    # drawings_list = db.relationship(lambda: Drawing)
    # files =

    @staticmethod
    def latest(num):
        return Project.query.order_by(desc(Project.id)).limit(num)


# class Drawing(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey(Project.id))
#     number = db.Column(db.Integer)
#     name = db.Column(db.String)
#     description = db.Column(db.String)
#     status = db.Column(db.String)
