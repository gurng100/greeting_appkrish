from flask import Blueprint, flash, request
from flask.templating import render_template
views = Blueprint(__name__,"views")

@views.route('/hello')
def index():
    flash("What's your name?")
    return render_template('index.html')

@views.route('/greet', methods=['POST',"GET"])
def greet():
    flash(f"Hello {str(request.form['name_input'])}, greet to see you.")
    return render_template('greet.html')

@views.route('/<name>')
def greet_name(name):
    flash(f"Hello {name}, greet to see you.")
    return render_template("greet.html")

