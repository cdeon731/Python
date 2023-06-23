from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # For validation messages
from flask_app.models import user

class Trail:
    db_name = "belt_review_schema" # CHANGE THIS TO MATCH YOUR SCHEMA NAME!  Class variable that holds the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.difficulty = data["difficulty"]
        self.description = data["description"]
        self.more_than_10_km = data["more_than_10_km"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
    
    # Adding a trail to the db
    @classmethod
    def add_trail(cls, data):
        query = """
        INSERT INTO trails 
        (name, location, difficulty, description, more_than_10_km, user_id)
        VALUES (%(name)s, %(location)s, %(difficulty)s,%(description)s, %(more_than_10_km)s, %(user_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Get all trails with users
    @classmethod
    def get_all_trails(cls):
        # Query to grab all trails WITH the users who added them
        query = """
        SELECT * FROM trails
        JOIN users 
        ON trails.user_id = users.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        # If we don't find any trails, we'll return an empty list
        if len(results) == 0:
            return []
        else: # Found at least 1 trail
            all_trail_objs = [] #This will hold trails
            # Loop through each dictionary in the list - trail_dictionary represents a different dictionary each time it gets passed through the results
            for trail_dictionary in results:
                # Create the trail (remember when creating a class object you must pass through a dictionary)
                trail_object = cls(trail_dictionary) # Using Trail(trail_dictionary) will also work
                # Grab the user's information
                user_dictionary = {
                    "id" : trail_dictionary["users.id"],
                    "first_name" : trail_dictionary["first_name"],
                    "last_name" : trail_dictionary["last_name"],
                    "email" : trail_dictionary["email"],
                    "password" : trail_dictionary["password"],
                    "created_at" : trail_dictionary["users.created_at"],
                    "updated_at" : trail_dictionary["users.updated_at"],
                }
                # Create the User object
                user_obj = user.User(user_dictionary)
                # Link this User to this Trail
                trail_object.user = user_obj
                # Add this Trail to the list of all trail objects
                all_trail_objs.append(trail_object)
            return all_trail_objs
    
    @classmethod
    def get_one_trail(cls, data):
        query = """
        SELECT * FROM trails
        JOIN users 
        ON trails.user_id = users.id
        WHERE trails.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        # If we don't find any trails, we'll return None - no trail
        if len(results) == 0:
            return None
        else: # Found 1 trail
            # No loop necessary
            trail_dictionary = results[0] # results is a list and with a SELECT query we get a list of dictionairies 
                                        # because we're passing through a dictionary we need to know the index of said dictionary and 
                                        # in this instance we are only selecting 1 trail so index [0] grabs that one trail for us
            # Create the trail (remember when creating a class object you must pass through a dictionary)
            trail_object = cls(trail_dictionary) # Using Trail(trail_dictionary) will also work
            # Grab the user's information
            user_dictionary = {
                "id" : trail_dictionary["users.id"],
                "first_name" : trail_dictionary["first_name"],
                "last_name" : trail_dictionary["last_name"],
                "email" : trail_dictionary["email"],
                "password" : trail_dictionary["password"],
                "created_at" : trail_dictionary["users.created_at"],
                "updated_at" : trail_dictionary["users.updated_at"],
            }
            # Create the User object
            user_obj = user.User(user_dictionary)
            # Link this User to this Trail
            trail_object.user = user_obj
            # Add this Trail to the list of all trail objects
        return trail_object

    @classmethod
    def update_trail(cls, data):
        query = """
        UPDATE trails SET
        name = %(name)s,
        location = %(location)s,
        difficulty = %(difficulty)s,
        description = %(description)s,
        more_than_10_km = %(more_than_10_km)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_trail(cls, data):
        query = "DELETE FROM trails WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)


    # Validations
    @staticmethod
    def validate_trail(form_data):
        is_valid = True
        print(form_data)
        if len(form_data["name"]) < 4:
            flash("Name must be 4 or more characters")
            is_valid = False
        if len(form_data["location"]) < 3:
            flash("Location must be 3 or more characters")
            is_valid = False
        if "difficulty" not in form_data or int(form_data["difficulty"]) < 1 or int(form_data["difficulty"]) > 5:
            flash("Difficulty must be between 1 and 5")
            is_valid = False
        if "more_than_10_km" not in form_data:
            flash("Please select whether the trail is 10 km")
            is_valid = False
        if len(form_data["description"]) < 10:
            flash("Description must be 10 or more characters")
            is_valid = False
        return is_valid