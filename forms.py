from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pets."""


name = StringField("Pet Name", validators=[InputRequired()])
species = StringField("Pet Species", choices=[
    ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
age = IntegerField("Pet Age", validators=[
    Optional(), NumberRange(min=0, max=30)])
notes = StringField("Additional Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Additional Notes")
    available = BooleanField("Available?")
