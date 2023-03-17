# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Friend:
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.occupation = data['occupation']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM friends;"
    results = connectToMySQL('first_flask').query_db(query)
    friends = []
    for friend in results:
      friends.append( cls(friend) )
    return friends

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM friends WHERE id = %(id)s ;"
    results = connectToMySQL('first_flask').query_db(query, data)
    
    user = cls(results[0])
  
    return user
            
  @classmethod
  def save(cls, data):
    query = "INSERT INTO friends ( first_name, last_name, occupation, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s, %(email)s, NOW(), NOW());"
    return  connectToMySQL('first_flask').query_db(query, data)
  
              
  @classmethod
  def update(cls, data):
    print(data)
    query = "UPDATE friends SET first_name=%(fname)s , last_name=%(lname)s, occupation=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
    return  connectToMySQL('first_flask').query_db(query, data)

            
  @classmethod
  def delete(cls, data):
    query = "DELETE FROM friends WHERE id = %(id)s;"
    return  connectToMySQL('first_flask').query_db(query, data)


  