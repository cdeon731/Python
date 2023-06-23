from flask_app import app
from flask import render_template, request, redirect, session # We'll import more here!
from flask_app.models import user, trail # REMEMBER TO IMPORT YOUR MODELS!!

@app.route("/trails")
def all_trails_page():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("all_trails.html", this_user= user.User.get_user_by_id(data), all_trails = trail.Trail.get_all_trails())

# Route that will show the new trail page
@app.route("/trails/new")
def new_trail_page():
    if "user_id" not in session:
        return redirect ("/")
    data = {
        "id": session["user_id"]
    }
    return render_template("add_trail.html", this_user= user.User.get_user_by_id(data))

# Route that will edit the trail page
@app.route("/trails/<int:id>/edit")
def edit_trail_page(id):
    if "user_id" not in session:
        return redirect ("/")
    data = {
        "id": id
    }
    return render_template("edit_trail.html", this_trail = trail.Trail.get_one_trail(data))

# Route that will show a trail
@app.route("/trails/<int:id>")
def view_trail_page(id):
    if "user_id" not in session:
        return redirect ("/")
    data = {
        "id": id
    }
    return render_template("view_trail.html", this_trail = trail.Trail.get_one_trail(data))

# Route that will delete a trail from the DB
@app.route("/trails/<int:id>/delete")
def delete_trail(id):
    if "user_id" not in session:
        return redirect ("/")
    data = {
        "id": id
    }
    trail.Trail.delete_trail(data)
    return redirect("/trails")

# Route to add trail to DB
@app.route("/trails/add_to_db", methods=["POST"])
def add_trail_to_db():
    if "user_id" not in session:
        return redirect ("/")
    # Validate to see if the trail form data looks good
    if not trail.Trail.validate_trail(request.form):
        return redirect("/trails/new")
    data = {
        "name" : request.form["name"],
        "location": request.form["location"],
        "difficulty" : request.form["difficulty"],
        "description" : request.form["description"],
        "more_than_10_km" : request.form["more_than_10_km"],
        "user_id" : session["user_id"],
    }
    trail.Trail.add_trail(data) # talk to the model to add the trail to db
    return redirect("/trails")

# Route to edit trail in db
@app.route("/trails/<int:id>/edit_in_db", methods=["POST"])
def edit_trail_in_db(id):
    if "user_id" not in session:
        return redirect ("/")
    # Validate to see if the trail form data looks good
    if not trail.Trail.validate_trail(request.form):
        return redirect(f"/trails/{id}/edit") #Important: REDIRECT TO CORRECT ROUTE (use an f string!)
    data = {
        "name" : request.form["name"],
        "location": request.form["location"],
        "difficulty" : request.form["difficulty"],
        "description" : request.form["description"],
        "more_than_10_km" : request.form["more_than_10_km"],
        "id" : id, #Note it's the id of the TRAIL, NOT the user
    }
    trail.Trail.update_trail(data) # talk to the model to add the trail to db
    return redirect("/trails")
