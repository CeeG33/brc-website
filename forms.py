from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """Contact us form."""
    name = StringField(label="Nom", validators=[DataRequired()])
    email = StringField(label="Adresse e-mail", validators=[
        DataRequired(), Email(granular_message=True)
    ])
    message = TextAreaField(label="Message", validators={DataRequired()})
    submit = SubmitField(label="Envoyer")