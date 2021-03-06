from enum import unique
from operator import methodcaller
from token import EXACT_TOKEN_TYPES
from unittest.util import _MAX_LENGTH
from application import app, db
from flask import Response, render_template, request, json, Response
from application.forms import LoginForm, RegisterForm
from application.models import User, Course, Enrollment

courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

@app.route('/')
def index():
    return render_template("index.html", loggedIn = True, index = True)

@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term = "2019"):
    return render_template("courses.html", courseData = courseData, courses = True, term = term)

@app.route('/register')
def register():
    return render_template("register.html", register = True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form = form, title = "Login", login = True)

@app.route('/enrollment', methods = ["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment = True, data={"courseID": id, "title": title, "term": term})

@app.route('/api/')
@app.route('/api/<idx>')
def api(idx = None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route('/user')
def user():
    #User(id=102, first_name="Khushboo", last_name="Verma", email="khushboo@abc.com", password="abc123").save()
    users = User.objects.all()
    return render_template('user.html', users=users)