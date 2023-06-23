from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import recipe
from flask_bcrypt import Bcrypt
import re	# the regex module
# create a regular expression object that we'll use later   
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def valid_user(cls, user):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        new_user = connectToMySQL('recipes_schema').query_db(query, user)
        return new_user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        user_data = connectToMySQL('recipes_schema').query_db(query)
        users = []
        for user in user_data:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_id(cls, user_id):
        data = {'id': user_id}
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod 
    def authenticated_user_input(cls, user_input):
        valid = True
        existing_user = cls.get_email(user_input["email"])
        password_valid = True

        if not existing_user:
            valid = False
        else:
            password_valid = bcrypt.check_password_hash(existing_user.password, user_input['password'])
            if not password_valid:
                valid = False
        if not valid:
            flash("That email & password combination does not match our records.")
            return False

        return existing_user

    @staticmethod
    def validate_registration(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query,user)
        if len(results) >= 1:
            flash("Email is alredy taken", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters", "register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords don't match", "register")
            is_valid = False
        return is_valid
    
