
#burgers.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
# from flask_app.models.ninja import Ninja

@app.route('/')
def index():
  return redirect("dojos")

@app.route('/dojos')
def dojos():
  dojos = Dojo.get_all()
  return render_template("index.html", all_dojos= dojos)

@app.route('/dojo/new',methods=['GET', 'POST'])
def create():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      "name":request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')
  #GET REQUEST
  dojos = Dojo.get_all()
  return render_template("index.html",  all_dojos= dojos)

@app.route('/dojos/<int:dojo_id>')
def detail_page(dojo_id):
  data = { 'id': dojo_id }
  cohort = Dojo.get_one_with_ninjas(data)
  # ninjas = []
  return render_template("results.html", cohort = cohort)
