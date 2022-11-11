import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import random

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# DB Models
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrolments = db.relationship('Enrolments', backref='students') # FK many to many Enrolments
    s_grades = db.relationship('Grades', backref='students') # FK ref Grades
    student_fname = db.Column(db.String(30), nullable=False)
    student_lname = db.Column(db.String(30), nullable=False)
    student_address1 = db.Column(db.String(50), nullable=False)
    student_address2 = db.Column(db.String(50), nullable=False)
    student_city = db.Column(db.String(30), nullable=False)
    student_county = db.Column(db.String(30), nullable=False)
    student_phone = db.Column(db.Integer, nullable=False)
    student_DOB = db.Column(db.Date, nullable=False)
    student_email = db.Column(db.String(50), nullable=False)
    student_password_ff = db.Column(db.String(50), nullable=False)
    authority_lvl = db.Column(db.Integer, nullable=False)


class Tutors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t_modules = db.relationship('Modules', backref='tutors') # FK ref Modules
    t_grades = db.relationship('Grades', backref='tutors') # FK ref Grades
    tutor_fname = db.Column(db.String(30), nullable=False)
    tutor_lname = db.Column(db.String(30), nullable=False)
    tutor_address1 = db.Column(db.String(50), nullable=False)
    tutor_address2 = db.Column(db.String(50), nullable=False)
    tutor_city = db.Column(db.String(30), nullable=False)
    tutor_county = db.Column(db.String(30), nullable=False)
    tutor_phone = db.Column(db.Integer, nullable=False)
    tutor_DOB = db.Column(db.DateTime, nullable=False)
    tutor_email = db.Column(db.String(50), nullable=False)
    tutor_password_ff = db.Column(db.String(50), nullable=False)
    authority_lvl = db.Column(db.Integer, nullable=False)


class Modules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrolments = db.relationship('Enrolments', backref='modules') # FK ref Enrolments
    m_tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'), nullable=False) # FK Tutors
    module_name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(50), nullable=False)


class Enrolments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrol_student_id = db.Column('student_id', db.Integer, db.ForeignKey('students.id')) # FK students
    enrol_module_id = db.Column('modules_id', db.Integer, db.ForeignKey('modules.id')) # FK modules
    enrol_grade_id = db.relationship('Grades', backref='enrolments', uselist=False) # FK ref Grades
    academic_year = db.Column(db.Date, nullable=False)


class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grades_student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False) # FK Students 
    grades_tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'), nullable=False) # FK Tutors
    grades_enrol_id = db.Column(db.Integer, db.ForeignKey('enrolments.id'), nullable=False)
    academic_year = db.Column(db.Date, nullable=False)
    ca1_score = db.Column(db.Integer)
    ca2_score = db.Column(db.Integer)
    exam_score = db.Column(db.Integer)


db.drop_all()
db.create_all()

# add to DB
for i in range(1,11):
    student = Students(student_fname = 'fname' + str(i),
    student_lname = 'lname' + str(i),
    student_address1 = 'address1 ' + str(i),
    student_address2 = 'address2 ' + str(i),
    student_city = 'city' + str(i),
    student_county = 'county' + str(i),
    student_phone =  random.randint(871111111, 879999999),
    student_DOB = date(year = random.randint(1960, 2004), month=random.randint(1, 12), day=random.randint(1, 28)),
    student_email = 'email_' + str(i) + '@gmail.com',
    student_password_ff = 'hash' + str(i),
    authority_lvl = 0)

    db.session.add(student)


for i in range(1,6):
    tutor = Tutors(tutor_fname = 'fname' + str(i),
    tutor_lname = 'lname' + str(i),
    tutor_address1 = 'address1 ' + str(i),
    tutor_address2 = 'address2 ' + str(i),
    tutor_city = 'city' + str(i),
    tutor_county = 'county' + str(i),
    tutor_phone =  random.randint(871111111, 879999999),
    tutor_DOB = date(year = random.randint(1960, 2004), month=random.randint(1, 12), day=random.randint(1, 28)),
    tutor_email = 'email_' + str(i) + '@gmail.com',
    tutor_password_ff = 'hash' + str(i),
    authority_lvl = 1)

    db.session.add(tutor)

for i in range(1,6):
    module = Modules(module_name = 'module ' + str(i),
    m_tutor_id = random.randint(1, 5), # foreign key !!!!!!!!!!!!!!!
    description = 'module description ' + str(i))

    db.session.add(module)

for i in range(1,51):
    enrolment = Enrolments(enrol_student_id = random.randint(1, 10), # foreign keys !!!!!!!!!!!!!!
    enrol_module_id = random.randint(1, 5),
    academic_year = date(year=2022, month=9, day=1))

    db.session.add(enrolment)

for i in range(1, 21):
    grade = Grades(grades_student_id = random.randint(1, 10), # foreign keys !!!!!!!!!!!!!!
    grades_tutor_id = random.randint(1, 5),
    grades_enrol_id = random.randint(1, 50),
    academic_year = date(year=2022, month=9, day=1),
    ca1_score = random.randint(0, 100),
    ca2_score = random.randint(1, 100),
    exam_score = random.randint(1, 100))

    db.session.add(grade)


db.session.commit()


'''
testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()
'''


@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)