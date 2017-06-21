from flask import Flask, request, redirect, render_template
import cgi
from http import cookies

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=['GET', 'POST'])

def signup():
    
    if request.method == 'GET':
        return render_template('index.html')
    C = cookies.SimpleCookie()
    C["username"] = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error=''
    verify_error=''
    email_error=''
    if C["username"].value == '' or ' ' in C["username"].value:
        username_error = "That's not a valid username"
    elif len(C["username"].value) < 3:
        username_error = "That username is too short"
    elif len(C["username"].value) > 20:
        username_error = "That username is too long"
    if password == ''  or ' ' in password:
        password_error = "That's not a valid password"
    elif len(password) < 3:
        password_error = "That password is too short"
    elif len(password) > 20:
        password_error = "That password is too long"
    if verify != password:
        verify_error = "Passwords don't match"
    count1 = email.count('@')
    count2 = email.count('.')
    if email is not "":
        if len(email) < 3 or len(email) > 20 or count1 != 1 or count2 != 1 or ' ' in email:
            email_error = "That's not a valid email"
    if not username_error and not password_error and not verify_error and not email_error:
        #return render_template('welcome.html', username=username)
        return redirect('/welcome?username={0}'.format(C["username"].value))
    else:
        #username=C["username"].value
        return render_template('index.html', username=C["username"].value, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome")
def welcome(): 
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()