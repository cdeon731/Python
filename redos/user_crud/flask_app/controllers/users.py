from flask import render_template, request, redirect
from flask_app.models.user import User
from flask_app import app

@app.route('/')
def all_users():
    return render_template('all_users.html', user=User.get_all())

@app.route('/create')
def new_user():
    return render_template('new_users.html')

@app.route('/create/new', methods=['POST'])
def create_user():
    User.save_user(request.form)
    return redirect('/')

@app.route('/view/<int:id>')
def view_user(id):
    data = {
        'id' : id
    }
    return render_template('view_users.html', user=User.get_one(data))

@app.route('/edit/<int:id>')
def edit_user(id):
    data = {
        'id' : id
    }
    return render_template('edit_users.html', user=User.get_one(data))

@app.route('/update', methods=['POST'])
def update():
    User.edit_user(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete_user(data)
    return redirect('/')
