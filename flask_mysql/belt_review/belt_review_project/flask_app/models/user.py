from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
# We'll be importing additional stuff here!
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# The lines below are for using bcrypt
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
from flask_app.models import trail

class User:
    db_name = "belt_review_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # Link to other classes here!
        self.trails = []

    # Add methods to create a new user and perhaps more!
    @classmethod
    def register_user(cls, data):
        query = """
        INSERT INTO users
        (first_name, last_name, email, password)
        VALUES 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None # Return None - no user found
        else:
            return cls(results[0]) # Create User object

    @classmethod
    def get_user_by_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            return cls(results[0]) # Create User object
    
    # Get all trails added by logged in user AND the user's info, regardless of how many trails were added by said user
    @classmethod
    def get_all_user_trails(cls, data):
        query = """
        SELECT * FROM users 
        LEFT JOIN trees 
        ON users.id = trees.user_id 
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) == 0:
            return []
        else:
            # Create the user object
            user_obj = cls(results[0])
            # Loop through each of our trails
            for this_trail in results:
                # Grab the trail's info
                trail_dictionary = {
                    "id": this_trail["trails.id"],
                    "name": this_trail["name"],
                    "location": this_trail["location"],
                    "difficulty": this_trail["difficulty"],
                    "description": this_trail["description"],
                    "more_than_10_km": this_trail["more_than_10_km"],
                    "created_at": this_trail["trails.created_at"],
                    "updated_at": this_trail["trails.updated_at"],
                }
                # Create the trail object
                trail_obj = trail.Trail(trail_dictionary)
                # Link this Trail to this User
                user_obj.trails.append(trail_obj)
            # Return this User with the Trails linked
            return user_obj


    # Validation login and registration here!
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        # Check first and last name
        if len(form_data["first_name"]) < 3:
            flash("First name must be 3 or more characters", "register")
            is_valid = False
        if len(form_data["last_name"]) < 3:
            flash("Last name must be 3 or more characters", "register")
            is_valid = False
        # Check email to make sure format matches
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        # Make sure email isn't taken already
        data = {
            "email": form_data["email"]
        }
        found_user_or_none = User.get_user_by_email(data)
        if found_user_or_none != None:
            flash("Email already taken", "register")
            is_valid = False
        # Password must be 8 or more characters
        if len(form_data["password"]) < 8:
            flash("Password must be 8 or more characters", "register")
            is_valid = False
        # Passwords must match
        if form_data["password"] != form_data["confirm_password"]:
            flash("Passwords don't agree", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data):
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid login credentials", "login") # Intentionally vague - so hackers aren't tipped off
            return False # Stop immediately - no need to check the password
        # Check to see if the email can be found
        data = {
            "email": form_data["email"]
        }
        found_user_or_none = User.get_user_by_email(data)
        if found_user_or_none == None:
            flash("Invalid login credentials", "login") # Intentionally vague - so hackers aren't tipped off
            return False # Stop immediately - no need to check the password
        # If the email is found, then check the password
        if not bcrypt.check_password_hash(found_user_or_none.password, form_data["password"]):
            flash("Invalid login credentials", "login") # Intentionally vague - so hackers aren't tipped off
            return False # Stop here
        # Return user object that we can use for session since the credentials are good
        return found_user_or_none