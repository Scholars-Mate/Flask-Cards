from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def login_or_redirect():
    pass

@app.route("/sets-home")
def sets_home():
    pass

@app.route("/settings")
def show_settings():
    pass

@app.route("/set/<int:setid>")
def show_set(setid):
    pass

@app.route("/set/<int:setid>/edit")
def edit_set(setid):
    pass
