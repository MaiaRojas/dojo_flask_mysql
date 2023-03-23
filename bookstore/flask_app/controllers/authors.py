# authors.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book
import pprint

@app.route('/')
def index():
  return redirect("/authors")

@app.route('/authors/new',methods=['GET', 'POST'])
def create():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      "fname":request.form['fname'],
      "lname":request.form['lname'],
    }
    Author.save(data)
    return redirect('/')
  #GET REQUEST
  authors = Author.get_all()
  print('Hereee', authors)
  return render_template("index.html", all_authors=authors)

@app.route('/authors')
def authors():
  authors = Author.get_all()
  return render_template("index.html", all_authors=authors)


@app.route('/authors/<int:author_id>')
def detail_author(author_id):
  data = {
    'id': author_id
  }
  favorites = Author.get_author_with_books(data)
  books = Book.get_books_not_favorites(data)
  return render_template("details_author.html", all_books = books, favorites=favorites)

@app.route('/favorites/authors/<int:author_id>', methods=['GET', 'POST'])
def favorite(author_id):
  #POST REQUEST
  if request.method == 'POST':
    data = {
      'author_id': author_id,
      'book_id': request.form['book_id'],
    }
    Book.add_favorite(data)
    return redirect(f'/authors/{author_id}')
  #GET REQUEST
  favorites = Author.get_author_with_books(data)
  books = Book.get_books_not_favorites(data)
  return render_template("details_author.html", all_books = books, favorites=favorites)
