from application import app, db
from flask import render_template
from application.models import Students, Tutors, Modules, Enrolments
from application.forms import RegistrationForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    txt = Students.query.first()
    return f'This is student city: {txt.student_city}'