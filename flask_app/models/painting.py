from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Painting:
    db_name = "painting"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.price = data["price"]
        self.quantity = data["quantity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all_Paintings(cls):
        query = "SELECT * FROM paintings"
        result = connectToMySQL(cls.db_name).query_db(query)
        paintings = []
        if result:
            for painting in result:
                paintings.append(painting)
            return paintings

    @classmethod
    def create(cls, data):
        query = "INSERT INTO paintings (title, description, price, quantity, user_id) VALUES (%(title)s, %(description)s, %(price)s,%(quantity)s,%(user_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_painting(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description=%(description)s, price = %(price)s, quantity = %(quantity)s  WHERE id = %(painting_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_painting(cls, data):
        query = "DELETE FROM paintings WHERE id = %(painting_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_painting_by_id(cls, data):
        query = "SELECT * FROM paintings LEFT JOIN users on paintings.user_id = users.id WHERE paintings.id = %(painting_id)s"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return result[0]
        return False

    @classmethod
    def delete_users_painting(cls, data):
        query = "DELETE FROM paintings WHERE paintings.user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def addBuy(cls, data):
        query = "INSERT INTO users_has_paintings (user_id, painting_id) VALUES (%(id)s, %(painting_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def removeBuy(cls, data):
        query = "DELETE FROM users_has_paintings WHERE painting_id = %(painting_id)s AND user_id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_users_who_buyed(cls, data):
        query = "SELECT user_id FROM users_has_paintings WHERE users_has_paintings.painting_id = %(painting_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        usersWhoBuyed = []
        if results:
            for person in results:
                usersWhoBuyed.append(person["user_id"])
        return usersWhoBuyed

    @classmethod
    def delete_all_buyed(cls, data):
        query = "DELETE FROM users_has_paintings WHERE painting_id = %(painting_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_painting(data):
        is_valid = True
        if len(data["title"]) < 3:
            flash("Title should be at least 3 characters!", "title")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description be at least 3 characters!", "description")
            is_valid = False
        if not data["price"]:
            flash("The price of the painting is required!", "price")
            is_valid = False
        if not data["quantity"]:
            flash("Quantity is required!", "quantity")
            is_valid = False
        return is_valid
