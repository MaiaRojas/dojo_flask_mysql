from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
  def __init__(self, data):
    self.id = data['id']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def save(cls, data):
    query = "INSERT INTO validation ( email, created_at, updated_at) VALUES (%(email)s, NOW(),NOW())"
    return connectToMySQL('validation').query_db(query,data)
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM validation ORDER BY `id` DESC;"
    results = connectToMySQL("validation").query_db(query)
    emails = []
    for email in results:
      emails.append(cls(email))
    return emails

  @classmethod
  def remove_email(cls,data): # remove relationship in burgers_toppings table
    query = "DELETE FROM validation WHERE validation.id = %(id)s ;"
    return connectToMySQL('validation').query_db(query,data);


  @staticmethod
  def validate(data):
    query = "SELECT * FROM validation WHERE email = %(email)s"
    result = connectToMySQL('validation').query_db(query, data)
    is_valid = True
    if not EMAIL_REGEX.match(data['email']): 
      flash("Invalid email address!")
      is_valid = False
    if result:
      flash('This email already exists')
      is_valid = False
    return is_valid
