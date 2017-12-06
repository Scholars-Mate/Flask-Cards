from flask import Flask, render_template, session, request
app = Flask(__name__)

@app.route("/")
def root():
    if session.get('userid'):
        return render_template('Homepage.html')
    else:
        session['userid'] = 'foo'
        return render_template('login.html')

@app.route("/login", methods = ['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return request.form['username']

app.secret_key ='aaa'
