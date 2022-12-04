import db
from command_logs import CommandLog
import session
import settings

db = db.DB(settings.SQLITE_DB_FILE)
table_name = "sessions"

# db.delete_table(table_name)
# db.create_table("sessions", "id INTEGER PRIMARY KEY, session_id TEXT, user_id TEXT,\
#                         expiry_date TEXT")

# db.create_table("commandlogs", "id INTEGER PRIMARY KEY, timestamp TEXT, user_id TEXT, command BLOB, response BLOB")

last_command = CommandLog.get_last_command(123)
last_response = CommandLog.get_last_response(123)

# last_command = CommandLog.get_last_command("123456")
# print(last_command)
# user_id = 123456789
# user_id2 = 1234567890
# user_id3 = 1234567891
# user_id4 = 1234567892
# mysession = session.Session(user_id=user_id)
# mysession2 = session.Session(user_id=user_id2)
# mysession3 = session.Session(user_id=user_id3)
# session.Session(user_id=user_id4)

# print(mysession.get_session())