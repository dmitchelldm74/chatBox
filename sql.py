import sqlite3

class SQL(object):
    def __init__(self, dbn):
        self.db = dbn
    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()  
    def execute(self, to_exec, return_):
        if return_ == True:
            try:
                return self.c.execute(to_exec) 
            except:
                self.c.execute(to_exec)   
        else:
            self.c.execute(to_exec)  
    def save(self):
        self.conn.commit()    
    def exit(self):
        self.conn.close()
    #c.execute('''CREATE TABLE stocks
    #             (date text, trans text, symbol text, qty real, price real)''')
    # INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)
    #symbol = 'RHAT'
    #c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
    #print c.fetchone()
    #for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    #    print row
    
    #conn.close()
