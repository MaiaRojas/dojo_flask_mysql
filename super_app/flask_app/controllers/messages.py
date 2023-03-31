from flask  import session, redirect, request

from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/post_message', methods=['POST'])
def post_message():
  if 'user_id' not in session:
    return redirect('/')

  data = {
    'content': request.form['content'],
    'sender_id': request.form['sender_id'],
    'reciver_id': request.form['reciver_id'],
  }

  Message.save(data)
  return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
  data = {
    'id': id
  }
  Message.destroy(data)
  return redirect('/dashboard')
