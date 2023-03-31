from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Message:
  db_name = 'super_app'
  def __init__(self, data):
    self.id = data['id']
    self.content = data['content']
    self.sender_id = data['sender_id']
    self.reciver_id = data['reciver_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.sender = data['sender']
    self.receiver = data['reciver']

  # 1) READ
  # 1.1) Get All User Messages
  @classmethod
  def get_user_messages(cls, data):
    query = 'SELECT users.first_name as sender, users2.first_name as reciver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.reciver_id WHERE users2.id = %(id)s'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    messages = []
    for message in results:
      messages.append(cls(message))
      print(message)
    return messages
  
  # 2) Create operations
  # 2.1) Create message
  @classmethod
  def save(cls, data):
    query = 'INSERT INTO messages (content, sender_id, reciver_id) VALUES (%(content)s, %(sender_id)s, %(reciver_id)s);'
    results = connectToMySQL(cls.db_name).query_db(query, data)
    return results
  
  # 3) Delete operations
  # 3.1) Delete message
  def destroy(cls, data):
    query = 'DELETE FROM messages WHERE messages.id = %(id)s;'
    return connectToMySQL(cls.db_name).query_db(query, data)

  # 4) Aux Method
  def time_span(self):
    now = datetime.now()
    delta = now - self.created_at
    print(delta.days)
    print(delta.total_seconds())
    if delta.days > 0:
      return f'{delta.days} days ago'
    elif (math.floor(delta.total_seconds() / 60)) >= 60:
      return  f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
    elif delta.total_seconds() >= 60:
      return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
    else:
      return f"{math.floor(delta.total_seconds())} seconds ago"
