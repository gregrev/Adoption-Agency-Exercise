from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange, Length


class AddPetForm(FlaskForm):
    """Form to add pets"""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="We need the pets name")])

    # species = StringField("Species", validators=[
    #     InputRequired(message="Please provide species"),
    #     AnyOf(["cat", "dog", "porcupine"], message="We now only accept cats, dogs, or porcupines for adoption.")])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField("Photo URL", validators=[URL(),
                                                     Optional()])

    age = IntegerField("Age", validators=[InputRequired(
        message="Please provide age"), NumberRange(min=0, max=30)])

    notes = TextAreaField("Notes", validators=[
        Optional(), Length(min=5)])


class EditPetForm(FlaskForm):
    """Form to edit existing pet"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
