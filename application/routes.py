from application import app, db
from application.models import Students, Tutors, Modules, Enrolments

@app.route('/')
@app.route('/home')
def home():
    txt = Students.query.first()
    print(txt)
    return f"This is student phone: {txt.student_phone}"

@app.route('/about')
def about():
    txt = Students.query.first()
    return f'This is student city: {txt.student_city}'