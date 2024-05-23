from flask_app.config.mysqlconnection import connectToMySQL



class Ninja:
    DB = 'dojos_and_ninjas'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']


    @classmethod
    def save(cls,data):
        query = "Insert INTO ninjas (first_name,last_name,age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        ninja_id = connectToMySQL(cls.DB).query_db(query,data)
        return ninja_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        if results:
            for ninja in results:
                ninjas.append(ninja)
        return ninjas


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos on ninjas.dojo_id = dojo.id WHERE ninjas.id = %(ninja_id)s;"
        results =  connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return results[0]
        return False
    

