import session

user_id = 123456789
user_id2 = 1234567890
user_id3 = 1234567891
mysession = session.Session(user_id=user_id, expiry_date="2021-01-01")
session.Session(user_id=user_id2, expiry_date="2021-01-01")
session.Session(user_id=user_id3, expiry_date="2021-01-01")


print(mysession.session_id)
print("Can we get the global sessions...")

print(session.GLOBAL_SESSION)

for i in session.GLOBAL_SESSION:
  if(i.user_id == user_id):
    print(i.session_id)