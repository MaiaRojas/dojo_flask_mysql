from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.validation import Email

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['GET','POST'])
def result():
  #POST REQUEST
  if request.method == 'POST':
    data = {
      'email': request.form['email'],
    }
    if not Email.validate(data):
      return redirect("/")
    print(Email.get_all())
    Email.save(data);
    return render_template("result.html", emails=Email.get_all())
  #GET REQUEST
  return render_template("result.html", emails=Email.get_all())

@app.route('/delete/<int:id>')
def delete(id):
  data = {
    'id': id
  }
  Email.remove_email(data)
  return redirect('/results')

if __name__ == "__main__":
    app.run(debug=True)