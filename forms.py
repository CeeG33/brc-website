from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    """Contact us form."""
    name = StringField("Nom", validators=[DataRequired()])
    email = StringField("Adresse email", validators=[
        Email(message=("Adresse mail non valide.")),
        DataRequired()])
    message = TextAreaField("Message", validators=[
        DataRequired(),
        Length(min=4, message=("Votre message est trop court."))])
    # recaptcha = RecaptchaField()