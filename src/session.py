import secrets
import datetime
import db
import settings

db = db.DB(settings.SQLITE_DB_FILE)
table_name = "sessions"

class Session:
  def __init__(self, user_id):
      self.user_id = user_id
      expiry_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
      self.expiry_date = expiry_date.strftime("%Y-%m-%d %H:%M:%S.%f")
      self.session_id = Session.create_session(user_id)
      self.save()

  def __str__(self): 
    return self.session_id

  def __repr__(self):
    return f"Session({self.user_id}, {self.expiry_date}, {self.session_id})"

  def save(self):
    # Save the session to the database

    # Check if the user has a session already
    query = f"user_id = '{self.user_id}'"
    result = db.select_query(table_name, "*", query)
    if result:
      # Update the session
      query = f"user_id = '{self.user_id}'"
      db.update_query(table_name, f"expiry_date = '{self.expiry_date}'", query)
    else:
      # Insert the session
      columns = "user_id, session_id, expiry_date"
      query = f"'{self.user_id}', '{self.session_id}', '{self.expiry_date}'"
      db.insert_query(table_name, columns, query)
  
  def delete(self):
    db.delete(table_name, f"session_id = '{self.session_id}'")

  def create_session(user_id):
    # Create a new session token
    random_session_id = secrets.token_hex(16)
    return random_session_id

  def get_session(self):
    # Get the session from the database
    query = f"user_id = '{self.user_id}'"
    result = db.select_query(self.table_name, "*", query)
    session_id = result[0][1]
    return session_id