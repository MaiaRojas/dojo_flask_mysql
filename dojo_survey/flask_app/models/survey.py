from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.location = data['location']
    self.language =  data['language']
    self.comment = data['comment']

  @classmethod
  def save(cls, data):
    query = "INSERT INTO surveys ( name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(),NOW())"
    return connectToMySQL('dojo_surveys').query_db(query,data)
  
  @classmethod
  def get_one(cls, data):
    query = "SELECT * FROM surveys  WHERE id=%(id)s;"
    results = connectToMySQL("dojo_surveys").query_db(query, data)
    return cls(results[0])

  @staticmethod
  def validate_survey(survey):
    is_valid = True
    if len(survey['name']) < 3:
      flash('Name must be at least 3 characters')
      is_valid = False
    if survey['location'] == '':
      flash('Must choose a favorite location')
      is_valid = False
    if survey['language'] == '':
      flash('Must choose a favorite language')
      is_valid = False
    if len(survey['comment']) < 3:
      flash('Comment must be at least 3 characters')
      is_valid = False
    return is_valid
