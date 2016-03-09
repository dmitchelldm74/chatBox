from sql import *
database = SQL('users.db')
database.connect()
database.execute('''CREATE TABLE embeded
                    (id text, user text, password text)''', False)
database.execute('''CREATE TABLE users
                    (user text, password text, email text, id real)''', False)
database.execute('''CREATE TABLE messages
                    (user text, message text, id text)''', False)
database.save()
database.exit()
