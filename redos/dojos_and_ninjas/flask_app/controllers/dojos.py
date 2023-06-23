from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def dojo():
    return render_template('create_dojo.html', dojos=Dojo.get_all())

@app.route('/create', methods=['POST'])
def create_dojo():
    Dojo.new_dojo(request.form)
    return redirect('/')

@app.route('/<int:id>')
def ninjas_in_dojo(id):
    data = {
        'id': id
    }
    return render_template('view_ninjas_at_dojo.html', dojo=Dojo.ninjas_at_dojo(data))
