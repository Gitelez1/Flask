from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request, session, flash


@app.route("/recipes/new")
def addrecipe():
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggeduser = User.get_user_by_id(data)
    return render_template("addRecipe.html", loggeduser=loggeduser)


@app.route("/add/recipe", methods=["POST"])
def createRecipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "datecooked": request.form["datecooked"],
        "instruction": request.form["instruction"],
        'user_id': session['user_id']
    }
    Recipe.create(data)
    return redirect("/")


@app.route("/recipe/<int:id>")
def viewRecipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"recipe_id": id, "id": session["user_id"]}
    recipe = Recipe.get_recipe_by_id(data)
    loggeduser = User.get_user_by_id(data)
    usersWhoLiked = Recipe.get_users_who_liked(data)
    return render_template("recipe.html", recipe=recipe, loggeduser=loggeduser, usersWhoLiked=usersWhoLiked, numOfLikes=len(Recipe.get_users_who_liked(data)))


@app.route("/delete/recipe/<int:id>")
def deleteRecipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"recipe_id": id, "id": session["user_id"]}
    recipe = Recipe.get_recipe_by_id(data)
    loggeduser = User.get_user_by_id(data)
    if recipe["user_id"] == loggeduser["id"]:
        Recipe.delete_all_likes(data)
        Recipe.delete_recipe(data)
    return redirect("/")


@app.route("/recipe/edit/<int:id>")
def editRecipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"recipe_id": id, "id": session["user_id"]}
    recipe = Recipe.get_recipe_by_id(data)
    if not recipe:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if recipe['user_id'] != loggeduser['id']:
        return redirect('/')
    return render_template("editRecipe.html", recipe=recipe, loggeduser=loggeduser)


@app.route("/update/recipe/<int:id>", methods=["POST"])
def updateRecipe(id):
    if "user_id" not in session:
        return redirect("/")
    data = {"recipe_id": id, "id": session["user_id"]}
    recipe = Recipe.get_recipe_by_id(data)
    if not recipe:
        return redirect('/')
    loggeduser = User.get_user_by_id(data)
    if recipe['user_id'] != loggeduser['id']:
        return redirect('/')
    if (
        len(request.form["name"]) < 1
        or len(request.form["description"]) < 1
        or len(request.form["datecooked"]) < 1
        or len(request.form["instruction"]) < 1
    ):
        flash("All fields required", "allRequired")
        return redirect(request.referrer)
    updateData={
        'name': request.form['name'],
        'description': request.form['description'],
        'datecooked': request.form['datecooked'],
        'instruction': request.form['instruction'],
        'recipe_id':id
    }
    if not Recipe.validate_recipe(updateData):
        return redirect(request.referrer)
    Recipe.update_recipe(updateData)
    return redirect('/recipe/'+ str(id))


@app.route('/like/<int:id>')
def addLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id': id,
        'id': session['user_id']
    }
    usersWhoLiked = Recipe.get_users_who_liked(data)
    if session['user_id'] not in usersWhoLiked:
        Recipe.addLike(data)
        return redirect(request.referrer)
    return redirect(request.referrer)

@app.route('/unlike/<int:id>')
def removeLike(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id': id,
        'id': session['user_id']
    }    
    Recipe.removeLike(data)
    return redirect(request.referrer)
