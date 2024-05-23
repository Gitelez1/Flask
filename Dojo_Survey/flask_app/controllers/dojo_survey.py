from flask_app import app
from flask import render_template, request, redirect, session, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['form_data'] = request.form
    return redirect(url_for('display_result'))

@app.route('/display_result')
def display_result():
    form_data = session.get('form_data', None)
    return render_template('dojo_result.html', form_data=form_data)

@app.route('/go_back', methods=['GET'])
def go_back():
    return redirect(url_for('index'))