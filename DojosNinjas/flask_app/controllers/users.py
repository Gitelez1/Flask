from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import User

@app.route("/")
def add():
    return render_template("create.html")

@app.route("/users")
def show():
    users = User.get_all()
    return render_template('read.html', users=users)

app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(data)
    return redirect('/users')