from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
  def __init__(self , data ):
    self.id = data['id']
    self.title = data['title']
    self.num_of_pages = data['num_of_pages']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un booke
    self.authors = []

  @classmethod
  def save( cls , data ):
    query = "INSERT INTO books ( title, num_of_pages, created_at , updated_at ) VALUES (%(title)s, %(pages)s,NOW(),NOW());"
    return connectToMySQL('bookstore').query_db( query, data)
  
  @classmethod
  def add_favorite(cls, data):
    query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
    return connectToMySQL('bookstore').query_db(query,data);

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM books;"
    results = connectToMySQL('bookstore').query_db(query)
    books = []
    for a in results:
      books.append(cls(a))
    return books

  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM books WHERE id = %(id)s;"
    author_from_db = connectToMySQL('bookstore').query_db(query,data)
    return cls(author_from_db[0])
  
  @classmethod
  def get_books_not_favorites(cls, data):
    query = 'SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s)'
    results = connectToMySQL('bookstore').query_db(query, data)
    books = []
    for a in results:
      books.append(cls(a))
    return books

  @classmethod
  def get_book_with_authors( cls , data ):
    query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
    results = connectToMySQL('bookstore').query_db( query , data )

    book = cls( results[0] )
    for row_from_db in results:
      author_data = {
        "id" : row_from_db["authors.id"],
        "first_name" : row_from_db["first_name"],
        "last_name" : row_from_db["last_name"],
        "created_at" : row_from_db["authors.created_at"],
        "updated_at" : row_from_db["authors.updated_at"]
      }
      book.authors.append( author.Author( author_data ) )
    return book