from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/home")
def recipes_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    data ={
        'id': session['user_id']
    }
    user = User.get_id(session["user_id"])
    recipes = Recipe.get_recipe()

    return render_template("recipes_home.html", user=user, recipes=recipes)

@app.route("/recipes/<int:recipe_id>")
def view_recipe(recipe_id):
    user = User.get_id(session["user_id"])
    recipe = Recipe.recipe_id(recipe_id)
    return render_template("view_recipes.html", user=user, recipe=recipe)

@app.route('/recipe/new')
def new_recipe():
    return render_template('new_recipes.html')

@app.route('/recipe/create', methods=['POST'])
def add_recipe():
    valid_recipe = Recipe.new_recipe(request.form)
    if valid_recipe:
        return redirect('/recipes/<int:recipe_id>')
    return redirect('/recipe/new')

@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    recipe = Recipe.recipe_id(recipe_id)
    return render_template("edit_recipes.html", recipe=recipe)

@app.route("/recipes/edit/<int:recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    valid_recipe = Recipe.update_recipe(request.form, session["user_id"])
    if not valid_recipe:
        return redirect("/recipes/edit/<int:recipe_id>")
        
    return redirect("/home")
