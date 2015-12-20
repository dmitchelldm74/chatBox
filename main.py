from flask import Flask, request, render_template

app = Flask(__name__)

#group = 'ccc'
#name = 'Daniel'

@app.route('/')
@app.route('/home')
def m():
    return render_template('home.html')
@app.route('/connect', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        s = '<!>'
        monkey = 'a'
        bananna = 'a'
        if monkey == bananna:
            f = open(group + '.txt', 'r')
            f3 = f.read()
            f.close()
            password2 = f3.split("<!>")
            print password2
            if password == password2[1]:
                f = open(group + ':inbox', 'r')
                f4 = f.read()
                f.close()
            return render_template('main.html', info=[f4, "<a href='/post'>Not Working? This is experimental so it still has issues... Click This and it should work!</a>"])  
        else:
            return "Sorry that was an incorrect username or password.&nbsp<a href='/connect'>Go Back>>></a>"  
     
@app.route('/create', methods = ['GET', 'POST'])
def form1():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        s = '<!>'
        group2 = request.form['group']
        password = request.form['password']
        f = open('groups.txt', 'a+')
        f.write(s + group2 + s)
        f.close()
        f = open(group2 + '.txt', 'w')
        f.write(s + password + s)
        f.close()
        f = open(group2 + ':inbox', 'w')
        f.close()
        return render_template('form.html')
        
@app.route('/post', methods = ['GET', 'POST'])
def form2():
    if request.method == 'GET':
        return render_template('main.html', info=["<a href='/connect'>Not Working? This is experimental so it still has issues... Click This and it should work!</a>"])
    elif request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        message = request.form['msg']
        s = '<!>'
        monkey = 'a'
        bananna = 'a'
        if monkey == bananna:
            f = open(group + '.txt', 'r')
            f3 = f.read()
            f.close()
            password2 = f3.split("<!>")
            print password2
            if password == password2[1]:
                if message == "":
                    f = open(group + ':inbox', 'r')
                    f4 = f.read()
                    f.close()
                else:
                    import datetime
                    senttime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
                    f = open(group + ':inbox', 'a+')
                    message2 = '<div class="panel-footer">' + '<b>@' + name + ':</b><br><br>' + message + '<br><br><b>' + senttime + '</b></div>'
                    f.write(message2)
                    f.close()
                    f = open(group + ':inbox', 'r')
                    f4 = f.read()
                    f.close()
                if message == '#del':
                    f = open(group + ':inbox', 'w')
                    f.truncate()
                    f.close()
        return render_template('main.html', info=[f4])    
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
