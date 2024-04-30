from flask_app import app
from flask import render_template

@app.route('/')
def index():
    users = (
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
);

    return render_template('index.html',user = users)