from flask import Flask, render_template
from forms import ContactForm
from dotenv import load_dotenv

SECRET_KEY = load_dotenv("SECRET_KEY")

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def home():
    """Renders the home page using the home.html file."""
    contact_form = ContactForm()
    return render_template("home.html", form=contact_form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
