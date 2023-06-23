from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.valid_user(data)
    session['user_id'] = id
    return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')