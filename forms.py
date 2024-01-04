from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """Contact us form."""
    name = StringField(label="Nom", validators=[DataRequired()])
    email = StringField(label="Adresse e-mail", validators=[
        DataRequired(), Email(granular_message=True)
    ])
    message = StringField(label="Message")
    submit = SubmitField(label="Envoyer")