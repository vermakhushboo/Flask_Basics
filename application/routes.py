from application import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", login=False)

@app.route('/hello')
def hello():
    return 'Hello, World'