from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
      self.id = data['id']
      self.first_name= data['first_name']
      self.last_name = data['last_name']
      self.age = data['age']
      self.dojo_id = data['dojo_id']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

    #1) READ OPERATIONS
    # 1.1) Get all ninjas 
    @classmethod
    def get_all(cls):
      query = "SELECT * FROM ninjas;"
      results =  connectToMySQL('dojos_ninjas').query_db(query)
      ninjas =[]
      for n in results:
        ninjas.append(cls(n))
      return ninjas

    # 2) CREATE OPERATIONS
    # 2.1) Create Ninja
    @classmethod
    def save(cls,data):
      query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s,NOW(),NOW())"
      results = connectToMySQL('dojos_ninjas').query_db(query,data)
      print('HEREEEE', results)
      return results

    @classmethod
    def get_one(cls,data):
      query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
      ninja_from_db = connectToMySQL('dojos_ninjas').query_db(query,data)
      return cls(ninja_from_db[0])

    @classmethod
    def update(cls,data):
      query = "UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s, updated_at = NOW() WHERE id = %(id)s;"
      return connectToMySQL('dojos_ninjas').query_db(query,data)

    @classmethod
    def destroy(cls,data):
      query = "DELETE FROM ninjas WHERE id = %(id)s;"
      return connectToMySQL('dojos_ninjas').query_db(query,data)
