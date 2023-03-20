from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
# from flask_app.models.ninja import Ninja

@app.route('/ninjas/new', methods=['GET', 'POST'])
def new_ninja():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      "fname":request.form['fname'],
      "lname":request.form['lname'],
      "age":request.form['age'],
      "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/dojos')
  #GET REQUEST
  dojos = Dojo.get_all()
  return render_template("new_ninja.html",  dojos = dojos)
