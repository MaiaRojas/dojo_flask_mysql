from urllib import request
from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/users")
def index():
  # llamar al método de clase get all para obtener todos los amigos
  friends = Friend.get_all()
  print(friends)
  return render_template("index.html", friends=friends)

@app.route('/add_user', methods=['POST'])
def add_user():
  data = {
    'fname': request.form['fname'],
    'lname': request.form['lname'],
    'email': request.form['email']
  }
  Friend.save(data)
  return redirect('/users')

@app.route('/users/new')
def create_friend():
  return render_template("add_user.html")
            
if __name__ == "__main__":

  app.run(debug=True)

