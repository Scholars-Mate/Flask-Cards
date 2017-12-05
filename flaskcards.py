from flask import Flask
app = Flask(__name__)
    import helpers.py 
    import database.py
@app.route("/")
def login_or_redirect():
    user = input('Enter userId: ');
    passw = input('Enter password: ');
    return logIn(user,passw);

@app.route("/sets-home")
def sets_home():
    user = input('Enter userId: ');
    return getSets(user);
    

@app.route("/settings")
def show_settings():
    
    pass

@app.route("/set/<int:setid>")
def show_set(setid):
    return getCards(setid);

@app.route("/set/<int:setid>/edit")
def edit_set(setid):
    name = input('Enter new set name: ');
    if(modifySet(setid,name))
    return true;
    else
    return false;
