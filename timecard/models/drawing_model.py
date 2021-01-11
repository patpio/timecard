from timecard import db


class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
