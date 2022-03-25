from application import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", loggedIn = True, index = True)

@app.route('/courses')
def courses():
    courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]
    print(courseData)
    return render_template("courses.html", courseData = courseData, courses = True)

@app.route('/register')
def register():
    return render_template("register.html", register = True)

@app.route('/login')
def login():
    return render_template("login.html", login = True)

@app.route('/hello')
def hello():
    return 'Hello, World'