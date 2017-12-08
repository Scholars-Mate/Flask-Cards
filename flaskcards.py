from flask import Flask, render_template, session, redirect, url_for, request, abort
import helpers
app = Flask(__name__)

@app.route("/")
def homepage_or_redirect():
    if session.get('userid') is None:
        return redirect(url_for('login'))
    sets = helpers.getSets(session.get('userid'))
    return render_template('Homepage.html', sets=sets)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if helpers.logIn(request.form['username'], request.form['password']):
            return redirect(url_for('homepage_or_redirect'))
        return render_template('login.html', login_fail=True)
    else:
        return render_template('login.html')

@app.route("/set/<int:setid>")
def show_set(setid):
    if session.get('userid') is None:
        return redirect(url_for('login'))

    cards = helpers.getCards(setid)
    return render_template('cardPreview.html', cards=cards, setid=setid)

@app.route("/signup", methods=['POST'])
def add_user():
    if helpers.addUser(request.form['username'], request.form['password'], request.form['fullname']):
        return redirect(url_for('login'))
    else:
        return render_template('login.html', usernameTaken=True)

@app.route("/addset", methods=['POST'])
def add_set():
    if session.get('userid') == None:
        abort(403)
    helpers.addSet(request.form['name'], request.form['category'])
    return redirect(url_for('homepage_or_redirect'))

@app.route("/editset", methods=['POST'])
def edit_set():
    if session.get('userid') == None:
        abort(403)
    helpers.editSet(request.form['setid'], request.form['name'], request.form['category'])
    return redirect(url_for('homepage_or_redirect'))

app.secret_key = ''
