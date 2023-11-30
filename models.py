from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://education.health.ufl.edu/files/2014/05/pet-sitting-pg.jpg"


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets available for adoption"""


__tablename__ = "pets"


id = db.Column(db.Integer, 
               primary_key=True)
name = db.Column(db.Text, nullable=False)
species = db.Column(db.Text, nullable=False)
photo_url = db.Column(db.Text, nullable=True)
age = db.Column(db.Integer, nullable=True)
notes = db.Column(db.Text, nullable=True)
available = db.Column(db.Boolean, nullable=False, default="True")


def image_url(self):
    """Return image for pet -- bespoke or generic."""

    return self.photo_url or GENERIC_IMAGE
