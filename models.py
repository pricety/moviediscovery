from app import db
from flask_login import UserMixin
from dataclasses import dataclass

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@dataclass
class Rating(db.Model):
    id: int
    rating: int
    comment: str
    username: str
    movie_id: int

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(200))
    username = db.Column(db.String(80))
    movie_id = db.Column(db.Integer)


db.create_all()
