from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
    db_name = "recipes"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.datecooked = data["datecooked"]
        self.instruction = data["instruction"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_Recipes(cls):
        query = "SELECT * FROM recipes"
        result = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        if result:
            for recipe in result:
                recipes.append(recipe)
            return recipes

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, datecooked, instruction, user_id) VALUES (%(name)s, %(description)s, %(datecooked)s,%(instruction)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description=%(description)s, datecooked = %(datecooked)s, instruction = %(instruction)s  WHERE id = %(recipe_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id = users.id WHERE recipes.id = %(recipe_id)s"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False

    @classmethod
    def delete_users_recipe(cls, data):
        query = "DELETE FROM recipes WHERE recipes.user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def addLike(cls, data):
        query = "INSERT INTO likes (user_id, recipe_id) VALUES (%(id)s, %(recipe_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removeLike(cls, data):
        query = "DELETE FROM likes WHERE recipe_id = %(recipe_id)s AND user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_users_who_liked(cls, data):
        query = "SELECT user_id from likes where likes.recipe_id = %(recipe_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        uswersWhoLiked = []
        if results:
            for person in results:
                uswersWhoLiked.append(person["user_id"])
        return uswersWhoLiked

    @classmethod
    def delete_all_likes(cls, data):
        query = "DELETE FROM likes where recipe_id = %(recipe_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Name should be at least 3 characters!", "name")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description be at least 3 characters!", "description")
            is_valid = False
        if not data["datecooked"]:
            flash("The date of the recipe is required!", "datecooked")
            is_valid = False
        if len(data["instruction"]) < 2:
            flash("Instructions should be at least 3 characters!", "instruction")
            is_valid = False
        return is_valid
