from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def page():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def detail_page(id):
    data = {
        "id": id
    }
    return render_template('ninja_show.html', dojo = Dojo.get_one(data))





