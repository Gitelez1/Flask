from flask_app import app
from flask import render_template, session, redirect, url_for, request


@app.route('/')
def index():
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    return render_template('index.html', visit_count=visit_count)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/click', methods=['POST'])
def increment():
    increment_by = int(request.form['click_by'])
    visit_count = session.get('visit_count', 0)
    visit_count += increment_by
    session['visit_count'] = visit_count
    return redirect(url_for('index'))