from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
  return redirect('/survey')

@app.route('/survey', methods=['GET','POST'])
def survey():
  return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def result():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      'name': request.form['name'],
      'location': request.form['location'],
      'language': request.form['language'],
      'comment': request.form['comment'],
    }
    if not Survey.validate_survey(data):
      return redirect("/survey")
    id = Survey.save(data)
    print('Createee',  id)
    data2 = {
      'id': id
    }
    survey = Survey.get_one(data2)
    print('hERE', survey)
    return render_template("result.html", survey=survey)
  #GET REQUEST
  return redirect('/survey')


if __name__ == "__main__":
    app.run(debug=True)