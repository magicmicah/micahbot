import datetime
import db
import settings

db = db.DB(settings.SQLITE_DB_FILE)
table_name = "commandlogs"

class CommandLog:
    table_name = "commandlogs"
    def __init__(self, user_id, command, response=None):
        self.user_id = user_id
        self.command = command
        self.response = response
        self.timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
        
        self.save()

    def create_table():
        db.create_table(table_name, "id INTEGER PRIMARY KEY, timestamp TEXT, user_id TEXT, command BLOB, response BLOB")

    def save(self):
        columns = "timestamp, user_id, command, response"
        query = f"'{self.timestamp}', '{self.user_id}', '{self.command}', '{self.response}'"
        db.insert_query(table_name, columns, query)

    def get_history(self):
        query = f"user_id = '{self.user_id}'"
        return db.select_query(table_name, "*", query)

    def delete_history(self):
        db.delete_query(table_name, f"user_id = '{self.user_id}'")

    def get_last_command(user_id):
        query = f"user_id = '{user_id}'"
        try:
            result = db.select_query(table_name, "*", query)
            return result[-1][3]
        except IndexError:
            return None

    def get_last_response(user_id):
        query = f"user_id = '{user_id}'"
        try:
            result = db.select_query(table_name, "*", query)
            return result[-1][4]
        except IndexError:
            return None
