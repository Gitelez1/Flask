from flask_app import app
from flask_app.models.painting import Painting
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request, session, flash


@app.route("/paintings/new")
def addpainting():
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggeduser = User.get_user_by_id(data)
    return render_template("addPainting.html", loggeduser=loggeduser)


@app.route("/add/painting", methods=["POST"])
def createPainting():
    if "user_id" not in session:
        return redirect("/")
    if not Painting.validate_painting(request.form):
        return redirect(request.referrer)
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "price": request.form["price"],
        "quantity": request.form["quantity"],
        'user_id': session['user_id']
    }
    Painting.create(data)
    return redirect("/")


@app.route("/painting/<int:id>")
def viewPainting(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    loggeduser = User.get_user_by_id(data)
    usersWhoBuyed = Painting.get_users_who_buyed(data)
    return render_template("painting.html", painting=painting, loggeduser=loggeduser, usersWhoBuyed=usersWhoBuyed, numOfByers=len(Painting.get_users_who_buyed(data)))


@app.route("/delete/painting/<int:id>")
def deletePainting(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    loggeduser = User.get_user_by_id(data)
    if painting["user_id"] == loggeduser["id"]:
        Painting.delete_all_likes(data)
        Painting.delete_painting(data)
    return redirect("/")


@app.route("/painting/edit/<int:id>")
def editPainting(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    if not painting:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if painting['user_id'] != loggeduser['id']:
        return redirect('/')
    return render_template("editPainting.html", painting=painting, loggeduser=loggeduser)


@app.route("/update/painting/<int:id>", methods=["POST"])
def updatePainting(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"painting_id": id, "id": session["user_id"]}
    painting = Painting.get_painting_by_id(data)
    if not painting:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if painting['user_id'] != loggeduser['id']:
        return redirect('/')
    if (
        len(request.form["title"]) < 1
        or len(request.form["description"]) < 1
        or len(request.form["price"]) < 1
        or len(request.form["quantity"]) < 1
    ):
        flash("All fields required", "allRequired")
        return redirect(request.referrer)
    updateData={
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity'],
        'painting_id':id
    }
    if not Painting.validate_painting(updateData):
        return redirect(request.referrer)
    Painting.update_painting(updateData)
    return redirect('/painting/'+ str(id))


@app.route('/buy/<int:id>')
def addBuy(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'painting_id': id,
        'id': session['user_id']
    }
    usersWhoBuyed = Painting.get_users_who_buyed(data)
    if session['user_id'] not in usersWhoBuyed:
        Painting.addBuy(data)
        return redirect(request.referrer)
    return redirect(request.referrer)

@app.route('/unbuy/<int:id>')
def removeBuy(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'painting_id': id,
        'id': session['user_id']
    }    
    Painting.removeBuy(data)
    return redirect(request.referrer)
