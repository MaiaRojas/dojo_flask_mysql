# books.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books/new',methods=['GET', 'POST'])
def create_book():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      "title":request.form['title'],
      "pages": request.form['pages'],
    }
    Book.save(data)
    return redirect('/books')
  #GET REQUEST
  books = Book.get_all()
  return render_template("books.html", all_books=books)

@app.route('/books')
def books():
  books = Book.get_all()
  return render_template("books.html", all_books=books)

@app.route('/books/<int:book_id>')
def detail_book(book_id):
  data = {
    'id': book_id
  }
  favorites = Book.get_book_with_authors(data)
  print('hERE', favorites.authors )
  authors = Author.get_authors_not_favorites(data)
  return render_template("details_book.html", all_authors = authors, favorites=favorites)

@app.route('/favorites/books/<int:book_id>', methods=['GET', 'POST'])
def favorite_book(book_id):
  #POST REQUEST
  if request.method == 'POST':
    data = {
      'author_id': request.form['author_id'],
      'book_id': book_id,
    }
    Book.add_favorite(data)
    return redirect(f'/books/{book_id}')
  #GET REQUEST
  favorites = Book.get_book_with_authors(data)
  authors = Author.get_authors_not_favorites(data)
  return render_template("details_author.html", all_authors = authors, favorites=favorites)
