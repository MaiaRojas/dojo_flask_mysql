from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
  def __init__(self,data):
    self.id = data['id']
    self.first_name= data['first_name']
    self.last_name= data['last_name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.books = []

  @classmethod
  def save(cls,data):
    query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(fname)s,%(lname)s,NOW(),NOW())"
    return connectToMySQL('bookstore').query_db(query,data)

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM authors;"
    results = connectToMySQL('bookstore').query_db(query)
    authors = []
    for a in results:
      authors.append(cls(a))
    return authors

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM authors WHERE authors.id = %(id)s;"
    author_from_db = connectToMySQL('bookstore').query_db(query,data)
    return cls(author_from_db[0])

  @classmethod
  def get_authors_not_favorites(cls, data):
    query = 'SELECT * FROM authors WHERE id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s)'
    results = connectToMySQL('bookstore').query_db(query, data)
    authors = []
    for a in results:
      authors.append(cls(a))
    return authors

  @classmethod
  def get_author_with_books( cls , data ):
    query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
    results = connectToMySQL('bookstore').query_db( query , data )

    author = cls( results[0] )
    for row in results:
      print('Here 14555', row)
      book_data = {
        "id" : row["book_id"],
        "title" : row["title"],
        "num_of_pages" : row["num_of_pages"],
        "created_at" : row["books.created_at"],
        "updated_at" : row["books.updated_at"]
      }
      author.books.append( book.Book( book_data ) )
    return author

  @classmethod
  def update(cls,data):
    query = "UPDATE authors SET name=%(name)s,updated_at = NOW() WHERE id = %(id)s;"
    return connectToMySQL('bookstore').query_db(query,data)

  @classmethod
  def destroy(cls,data):
    query = "DELETE FROM authors WHERE id = %(id)s;"
    return connectToMySQL('bookstore').query_db(query,data)
