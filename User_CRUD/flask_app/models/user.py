from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = "userscd"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        if results:
            for user in results:
                users.append(user)
            return users

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);" 
        return connectToMySQL(cls.db_name).query_db(query,data)

    classmethod
    def delete (cls,data):
        query = "DELETE FROM users Where id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if results:
            return results[0]
        return False

