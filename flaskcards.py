from flask import Flask, render_template, session, request, redirect, url_for
import helpers
app = Flask(__name__)


@app.route("/")
def root():
    if session.get('userid'):
        return render_template('Homepage.html')
    else:
        return redirect('/login')

@app.route("/login", methods = ['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if helpers.logIn(request.form['username'], request.form['password']):
            return redirect(url_for('root'))
        return render_template('login.html', login_fail=True)
		
@app.route("/sign-up", methods = ['GET', 'POST'])
def signup_user():
	helpers.addUser(request.form['newUsername'],request.form['newPassword'],request.form['newFullName'])
	return redirect(url_for('show_login'))
    
@app.route("/about", methods = ['GET'])
def show_about():
	return render_template('about.html')

	
@app.route("/home", methods = ['POST'])
def show_home():
	if session.get('userid'):
		return helpers.getSets('userid')
	else:
		return redirect('/login')

@app.route("/set/<int:setid>", methods = ['POST'])
def show_set(setid):
	return helpers.getCards('setid')
	
@app.route("/set/<int:setid>/edit", methods = ['POST'])
def edit_set(setid):
	if request.method == 'POST' :
		helpers.modifySet(setid, request.form['newName'])
		
		
@app.route("/cardPreview", methods = ['POST'])
def previewCard():
	return render_template('cardPreview.html')

	
app.secret_key ='aaa'
