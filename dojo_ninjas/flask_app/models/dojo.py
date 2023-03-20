from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
  def __init__(self , data ):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un dojoe
    self.ninjas = []

  # 1) READ OPERATIONS
  # 1.1) Get all dojos without ninjas

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM dojos;'
    results = connectToMySQL('dojos_ninjas').query_db(query)
    dojos = []
    for dojo in results:
      dojos.append(cls(dojo))
    return dojos

  # 1.2 ) Get one dojo
  @classmethod
  def get_one(cls, data):
    query = 'SELECT * FROM dojos WHERE id=%(id)s;'
    results = connectToMySQL('dojos_ninjas').query_db(query, data)
    print('HERE 2', results[0])
    return cls(results[0])

  # 1.3) Get One dojo with ninjs
  @classmethod
  def get_one_with_ninjas(cls, data):
    query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(id)s;'
    results = connectToMySQL('dojos_ninjas').query_db(query, data)
    cohort = cls(results[0])
    for row in results:
      ninja_data = {
        'id': row['id'],
        'first_name': row['first_name'],
        'last_name': row['last_name'],
        'age': row['age'],
        'dojo_id': row['dojo_id'],
        'created_at': row['created_at'],
        'updated_at': row['updated_at'],
      }
      cohort.ninjas.append(ninja.Ninja(ninja_data))
    return cohort

  # 2) CREATE OPERATIONS
  # 2.1) Create dojo
  @classmethod
  def save( cls , data ):
    query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
    results = connectToMySQL('dojos_ninjas').query_db( query, data)
    return results
