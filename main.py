from flask import Flask, request, render_template
import os.path
#a = os.path.isfile(name)
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
        ie = 'get'
        return render_template('form.html')
    elif request.method == 'POST':
        name = request.form['name']
        group = request.form['group']
        password = request.form['password']
        ie = 'post'
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
        maile = request.form['email']
        a = os.path.isfile(group2 + ':inbox')
        if a == False:
            f = open('email.txt', 'a+')
            f.write(maile)
            f.close()
            f = open('groups.txt', 'a+')
            f.write(s + group2 + s)
            f.close()
            f = open(group2 + '.txt', 'w')
            f.write(s + password + s)
            f.close()
            f = open(group2 + ':inbox', 'w')
            f.close()
            return render_template('form.html')
        else:    
            return "<font color='red'>Group Already Exists!</font>&nbsp;<a href='/create'>Back</a>"
        
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
                    message2 = '<div class="panel-footer">' + '<b>@' + name + '</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>Sent At:&nbsp;' + senttime + '</i><br><br>' + message + '<br><br></div>'
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
        a = 's'
        b = 's'
        if a == b:
            import random
            on = random.randint(0, 1000)
            on2 = random.randint(0, 2000)
            on3 = random.randint(0, 3000)
            onh = 'anf' + str(on) + 'fhgjk' + str(on2) + 'kjslf' + str(on3)
            a = os.path.isfile(onh)  
            if a == True:
                on = random.randint(0, 1000)
                on2 = random.randint(0, 2000)
                on3 = random.randint(0, 3000)
                onh = 'anf' + str(on) + 'fhgjk' + str(on2) + 'kjslf' + str(on3)
                a = os.path.isfile(onh)
                j = open(onh, "w")
                j.write("<!>" + ln[1] + "<!>" + ln[2] + "<!>" + ln[0] + "<!>")
                j.close() 
                c23 = '<iframe src="http://162.243.6.91:5000/' + onh + '"></iframe>' 
            else:
                j = open(onh, "w")
                j.write("<!>" + ln[1] + "<!>" + ln[2] + "<!>" + ln[0] + "<!>")
                j.close() 
                c23 = '<iframe src="http://162.243.6.91:5000/' + onh + '"></iframe>'  
        
        return render_template('embed.html', c=c23)   
                
@app.route('/inbox/<group>/<password>', methods = ['GET', 'POST'])
def form876(group, password):
    if request.method == 'GET':
        f = open(group + '.txt', "r")
        f2 = f.read()
        f.close()
        f3 = f2.split("<!>")
        if password == f3[1]:
            f = open(group + ':inbox', "r")
            f4 = f.read()
            f.close()
        else:
            f4 = "<font color='red'>Nice try hackers...Login failed!</font>"        
        return render_template('source.html', info=[f4])
    elif request.method == 'POST':
        group2 = request.form['nm']
        f = open(group2, 'r')
        f2 = f.read()
        f.close()   
        return f2
        
@app.route('/<number>')
def numer(number): 
    f = open(number, "r")
    f2 = f.read()
    f3 = f2.split("<!>")
    f.close()
    f = open(f3[1] + '.txt', 'r')
    f4 = f.read()
    f5 = f4.split("<!>")
    f.close()
    if f3[2] == f5[1]:
        f = open(f3[1] + ':inbox', 'r')
        f6 = f.read()
        f.close()
    else:
        f6 = "Login Failed..."    
    return render_template('source.html', info=[f6])        
             
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
