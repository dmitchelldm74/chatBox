# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import os.path
import sqlite3
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def m():
    return render_template('home.html')
@app.route('/connect', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        ie = 'get'
        return render_template('form.html')
    elif request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        ie = 'post'
        s = '<!>'
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        print c.execute('SELECT password FROM users WHERE user = ?', (group,))
        for it in c.execute('SELECT password FROM users WHERE user = ?', (group,)):
            if password == it[0]:
                f4 = ""
                text2 = 'SELECT message FROM messages WHERE user = "%s"' % group
                for message in c.execute(text2):
                    f4 = f4 + message[0]  
                return render_template('main.html', info=[f4, "<a href='/post'>Not Working? This is experimental so it still has issues... Click This and it should work!</a>"])  
            else:
                return "Sorry that was an incorrect username or password.&nbsp<a href='/connect'>Go Back>>></a>"  
     
@app.route('/create', methods = ['GET', 'POST'])
def form1():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        s = '<!>'
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        group2 = request.form['group']
        password = request.form['password']
        maile = request.form['email']
        #print group2, password, maile
        #database.execute("INSERT INTO users VALUES ('Daniel','mom1','dmitchell.dm74@gmail.com', 98727)", False)
        a = False
        try:
            for row in c.execute('SELECT password FROM users WHERE user = ?', (group2,)):
                try:
                    print row[0]
                    a = True
                except:
                    a = False
        except:
            a = False
        if a == False:
            #text2 = "INSERT INTO users VALUES ('%s','%s','%s', 0)" % (group2, password, maile)
            c.execute("INSERT INTO users VALUES (?, ?, ?, 0)", (group2, password, maile))
            conn.commit()
            conn.close()
            return render_template('form.html')
        else:    
            return "<font color='red'>Group Already Exists!</font>&nbsp;<a href='/create'>Back</a>"
        
@app.route('/post', methods = ['GET', 'POST'])
def form2():
    if request.method == 'GET':
        return render_template('main.html', info=["<a href='/connect'>Not Working? This is experimental so it still has issues... Click This and it should work!</a>"])
    elif request.method == 'POST':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        message = request.form['msg']
        text = 'SELECT password FROM users WHERE user = "%s"' % group
        o = message.replace("://", "$-link-$://").split("://")
        link = ""
        messages = ""
        import random
        idd = name + str(random.randint(0, 9999999999999999999999)) + group
        for it in o:
            print it
            if "$-link-$" in it:
                link = "<a href='" + it.replace("$-link-$", "://")
            else:
                o2 = it.split(" ")
                rest = ""
                i = len(o2) - 1
                i2 = 1
                while i2 <= i:
                    rest = rest + " " + o2[i2]
                    i2 = i2 + 1
                http = link + o2[0]
                
                end = "</a>"
                if "://" in link:
                    link = http + "'>" + o2[0] + end
                else:
                    link = o2[0]
                messages = messages + link + rest
                link = ""
                print o2
        for use in c.execute(text):
            if password == use[0]:
                    import datetime
                    senttime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
                    message2 = '<div class="panel-footer">' + '<b>@' + name + '</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>Sent At:&nbsp;' + senttime + '</i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/delete/' + group + '/' + password + '/' + idd + '"><font color="red">DELETE!</font></a><br><br>' + message + '<br><br></div>'
                    c.execute("INSERT INTO messages VALUES (?,?,?)",(group, message2, idd))
                    conn.commit()
                    f4 = ""
                    text2 = 'SELECT message FROM messages WHERE user = "%s"' % group
                    for message in c.execute(text2):
                        f4 = f4 + message[0]
                    return render_template('main.html', info=[f4]) 
            else:
                return render_template('main.html', info=["<font color='red'>INVALID PASSWORD!</font>"])
@app.route('/generate')
def gen(): 
    return render_template('generate.html')
    
@app.route('/from-url')
def adgen(): 
    return render_template('fu.html')
    
@app.route('/simple-from-url')
def adgen2(): 
    return render_template('fu2.html')    

@app.route('/contacts')
def adgen8(): 
    return render_template('contacts.html')
        
@app.route('/addins')
def adins():
    return render_template('add-ins.html')
@app.route('/embed', methods = ['GET', 'POST'])
def embed():
    if request.method == 'GET':
        ie = ''
        return render_template('embed.html', c=ie)
    elif request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        ln = [name, group, password]
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        for text in c.execute('SELECT password FROM users WHERE user = "%s"' % group):
            if password == text[0]:
                import random
                on = random.randint(0, 1000)
                on2 = random.randint(0, 2000)
                on3 = random.randint(0, 3000)
                onh = 'anf' + str(on) + 'fhgjk' + str(on2) + 'kjslf' + str(on3)
                a = os.path.isfile(onh)
                c.execute("INSERT INTO embeded VALUES (?,?,?)",(onh, ln[1], ln[2]))
                c23 = '<iframe src="http://162.243.6.91:5000/' + onh + '"></iframe>' 
                conn.commit()
        return render_template('embed.html', c=c23)   
                
@app.route('/inbox/<group>/<password>', methods = ['GET', 'POST'])
def form876(group, password):
    if request.method == 'GET':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        text = 'SELECT password FROM users WHERE user = "%s"' % group
        for use in c.execute(text):
            if password == use[0]:
                text2 = 'SELECT message FROM messages WHERE user = "%s"' % group
                f4 = ""
                for message in c.execute(text2):
                    f4 = f4 + message[0]
            else:
                f4 = "<font color='red'>Nice try hackers...Login failed!</font>"        
        return render_template('source.html', info=[f4])
    '''elif request.method == 'POST':
        group2 = request.form['nm']
        f = open(group2, 'r')
        f2 = f.read()
        f.close()   
        return f2'''
        
@app.route('/<number>')
def numer(number): 
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    for text in c.execute('SELECT * FROM embeded WHERE id = ?', (number,)):
        for ps in c.execute('SELECT password FROM users WHERE user = ?', (text[1],)):
            text2 = 'SELECT message FROM messages WHERE user = "%s"' % text[1]
            if text[2] == ps[0]:
                f6 = ""
                for message in c.execute(text2):
                    f6 = f6 + message[0]
            else:
                f6 = "Login Failed..."    
    return render_template('source.html', info=[f6])        

@app.route('/delete/<boxn>/<ps>/<idn>')
def delete(boxn, ps, idn): 
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    text = 'SELECT password FROM users WHERE user = "%s"' % boxn
    for use in c.execute(text):
        if ps == use[0]:
            text2 = 'DELETE FROM messages WHERE id = "%s"' % idn
            c.execute(text2)
            conn.commit()
            f4 = ""
            text3 = 'SELECT message FROM messages WHERE user = "%s"' % boxn
            for message in c.execute(text3):
                f4 = f4 + message[0]
    return render_template('source.html', info=[f4])             
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5555)
