from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja

@app.route('/ninja')
def new_ninja():
    return render_template('create_ninja.html', dojos=dojo.Dojo.get_all() )

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.new_ninja(request.form)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_ninja(id):
    data = {
        'id': id
    }
    return render_template('edit_ninjas.html', ninja=Ninja.get_one(data))

@app.route('/update', methods=['POST'])
def update():
    Ninja.edit_ninja(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = {
        'id' : id
    }
    Ninja.delete_ninja(data)
    return redirect('/')

