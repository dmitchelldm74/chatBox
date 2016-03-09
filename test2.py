import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()
#c.execute("INSERT INTO users VALUES ('%s', '%s', '%s', 0)" % ("Daniel", "mom1", "dmitchell.dm74@gmail.com"))
c.execute("INSERT INTO users VALUES (?, ?, ?, 0)", ("Anna", "anna", "anna@droplet.com"))
conn.commit()
