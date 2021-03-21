"""Server for HeartMovies"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined


app = Flask(__name__)


@app.route('/')
def display_homepage():
    """Shows the homepage."""

    return render_template('index.html')




if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port='5000', debug=True)