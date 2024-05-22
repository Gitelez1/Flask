from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    DB = 'dojos_and_ninjas'
    def __init__( self , data ):
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id= data['id']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for eachDojo in results:
            dojos.append( cls(eachDojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0])
        for b in results:
            eachDojo = {
                'id': b['ninjas.id'],
                'first_name': b['first_name'],
                'last_name': b['last_name'],
                'age': b['age'],
                'created_at': b['ninjas.created_at'],
                'updated_at': b['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(eachDojo))
        return dojo
