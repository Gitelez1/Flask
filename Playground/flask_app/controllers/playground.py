
from flask import app
from flask import render_template


@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:num>')
def play_x(num):
    return render_template("index_num.html", num=int(num))

@app.route('/play/<int:num>/<color>')
def play_x_boxes(num, color):
    return render_template('index_num_color.html', num=int(num), color=color)
