from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
    
    # @classmethod
    # def get_recipe(cls):
    #     query = "SELECT * FROM recipes;"
    #     user_data = connectToMySQL('recipes_schema').query_db(query)
    #     recipes = []
    #     for row in user_data:
    #         recipes.append( cls(row) )
    #     return recipes

    @classmethod
    def new_recipe(cls, recipes):
        if not cls.validate_recipe(recipes):
            return False
        query = """ 
        INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);
        """
        recipe_id = connectToMySQL("recipes_schema").query_db(query, recipes)
        recipe = cls.recipe_id(recipe_id)
        return recipe
    
    @classmethod
    def recipe_id(cls, recipe_id):
        data = {
            'id': recipe_id
        }
        query = """
        SELECT recipes.id, name, instructions, description, date_made, under_30, recipes.created_at, recipes.updated_at,
        users.id, first_name, last_name, email, users.created_at, users.updated_at
        FROM recipes 
        JOIN users on users.id = recipes.user_id 
        WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL('recipes_schema').query_db(query, data)
        result = result[0]
        recipe = cls(result)
        recipe.user = user.User(
                {
                    "id": result["users.id"],
                    "first_name": result["first_name"],
                    "last_name": result["last_name"],
                    "email": result["email"],
                    "created_at": result["users.created_at"],
                    "updated_at": result["users.updated_at"]
                }
            )
        return recipe

    @classmethod
    def update_recipe(cls, recipes, session_id):
        recipe = cls.recipe_id(recipes["id"])
        if recipe.user.id != session_id:
            flash("You must be the creator to update this recipe.")
            return False

        if not cls.validate_recipe(recipes):
            return False

        query = """UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, 
                    date_made=%(date_made)s, under_30 = %(under_30)s
                    WHERE id = %(id)s;"""
        result = connectToMySQL("recipes_schema").query_db(query, recipes)
        recipe = cls.recipe_id(recipes["id"])
        return recipe
    
    @classmethod
    def get_all(cls):
        query = """SELECT recipes.id, name, description, instructions, date_made, under_30, recipes.created_at, recipes.updated_at,
                    users.id, first_name, last_name, email, users.created_at, users.updated_at
                    FROM recipes JOIN users on users.id = recipes.user_id;
                    """
        recipe_data = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in recipe_data:
            recipe_user = cls(recipe)
            recipe_user.user = user.User(
                {
                    "id": recipe["users.id"],
                    "first_name": recipe["first_name"],
                    "last_name": recipe["last_name"],
                    "email": recipe["email"],
                    "created_at": recipe["users.created_at"],
                    "updated_at": recipe["users.updated_at"]
                }
            )
            recipes.append(recipe_user)
        return recipes

    @staticmethod
    def validate_recipe(recipes):
        is_valid = True
        if len(['name']) < 3:
            flash("Name not long enough")
            is_valid = False
        if len(recipes['description']) < 3:
            flash("Description not long enough")
            is_valid = False
        if len(recipes['instructions']) < 3:
            flash("Instructions not long enough")
            is_valid = False
        if len(recipes['date_made']) <= 0:
            flash("Date is required")
            is_valid = False
        if 'under_30' not in recipes:
            flash("Select yes or no for 'Under 30 mins?'")
            is_valid = False
        return is_valid