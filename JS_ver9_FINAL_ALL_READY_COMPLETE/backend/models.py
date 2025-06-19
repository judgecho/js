from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    exam_id = db.Column(db.Integer, nullable=False)
    answers = db.Column(db.PickleType, nullable=False)
    score = db.Column(db.Float, default=0.0)