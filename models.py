#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member

"""
file containing database tables
"""

from dataclasses import dataclass
from flask_login import UserMixin
from app import db

# pylint: disable=too-few-public-methods
class User(db.Model, UserMixin): # pylint: disable=missing-class-docstring
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@dataclass
class Rating(db.Model): # pylint: disable=missing-class-docstring
    id: int # pylint: disable=invalid-name
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
