from urllib import request
from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/users')

@app.route("/users")
def get_users():
  # llamar al método de clase get all para obtener todos los amigos
  friends = Friend.get_all()
  print(friends)
  return render_template("index.html", friends=friends)

@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
  # POSTT REQUEST
  if request.method == 'POST':
    data = {
      'fname': request.form['fname'],
      'lname': request.form['lname'],
      'email': request.form['email']
    }
    Friend.save(data)
    return redirect('/users')

  return render_template('add_user.html')

@app.route('/users/<int:user_id>')
def users_details(user_id):
  data = {
    'id': user_id
  }
  user = Friend.get_one(data);
  return render_template('user_detail.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'post'])
def edit_user(user_id):
  #POST request
  if request.method == 'POST':
    data = {
      'id': user_id,
      'fname': request.form['fname'],
      'lname': request.form['lname'],
      'email': request.form['email']
    }
    Friend.update(data)
    return redirect('/users')

  #GET REQUEST
  data = {
    'id': user_id
  }
  user = Friend.get_one(data)
  return render_template('edit_user.html', user= user)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id,
    }
    Friend.delete(data)
    return redirect('/users')


if __name__ == "__main__":

  app.run(debug=True)

