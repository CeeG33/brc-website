import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from flask_mail import Mail, Message
from forms import ContactForm
from flask_bootstrap import Bootstrap

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = os.getenv("MAIL_PORT")
MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
RECIPIENT_MAIL = os.getenv("RECIPIENT_MAIL")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = SECRET_KEY

mail = Mail()
app.config["MAIL_SERVER"] = MAIL_SERVER
app.config["MAIL_PORT"] = MAIL_PORT
app.config["MAIL_USE_SSL"] = MAIL_USE_SSL
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
mail.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():
    """Renders the home page using the home.html file"""
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        msg = Message(
            "Message du formulaire de contact",
            sender=MAIL_USERNAME,
            recipients=[RECIPIENT_MAIL],
        )
        msg.body = f"Nom : {name} - Email : {email} - Message : {message}"

        mail.send(msg)

        return render_template("home.html", success=True)
    
    else:
        
        return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
