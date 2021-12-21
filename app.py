
from flask import Flask, render_template, request
import pickle


# Initialise the Flask app
app = Flask(__name__)


# Set up the main route
@app.route('/', methods=["GET", "POST"])
def main():
        # We now pass on the input from the from and the prediction to the index page
        return render_template("index.html")
    # If the request method is GET
