from flask import Flask, redirect, url_for
from forms import RegistrationForm
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('.env')

app.debug = config['DEFAULT']['DEBUG']
app.secret_key = config['DEFAULT']['SECRET_KEY']

@app.route("/")
def login():
    return redirect(url_for('signup'))

@app.route("/signup")
def signup():
    return "En registro"

if __name__ == "__main__":
    app.run()