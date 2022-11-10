import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# DB Models
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_fname = db.Column(db.String(30), nullable=False)
    student_lname = db.Column(db.String(30), nullable=False)
    student_address1 = db.Column(db.String(50), nullable=False)
    student_address2 = db.Column(db.String(50), nullable=False)
    student_city = db.Column(db.String(30), nullable=False)
    student_county = db.Column(db.String(30), nullable=False)
    student_phone = db.Column(db.Integer, primary_key=True)
    student_DOB = db.Column(db.Date, nullable=False)
    student_email = db.Column(db.String(50), nullable=False)
    student_password_ff = db.Column(db.String(50), nullable=False)
    authority_lvl = db.Column(db.Integer, nullable=False)


class Tutors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tutor_fname = db.Column(db.String(30), nullable=False)
    tutor_lname = db.Column(db.String(30), nullable=False)
    tutor_address1 = db.Column(db.String(50), nullable=False)
    tutor_address2 = db.Column(db.String(50), nullable=False)
    tutor_city = db.Column(db.String(30), nullable=False)
    tutor_county = db.Column(db.String(30), nullable=False)
    tutor_phone = db.Column(db.Integer, primary_key=True)
    tutor_DOB = db.Column(db.Date, nullable=False)
    tutor_email = db.Column(db.String(50), nullable=False)
    tutor_password_ff = db.Column(db.String(50), nullable=False)
    authority_lvl = db.Column(db.Integer, nullable=False)


class Modules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(30), nullable=False)
    m_tutor_id = db.Column(db.Integer) # foreign key !!!!!!!!!!!!!!!
    description = db.Column(db.String(50), nullable=False)


class Enrolment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrol_student_id = db.Column(db.Integer) # foreign keys !!!!!!!!!!!!!!
    enrol_module_id = db.Column(db.Integer)
    academic_year = db.Column(db.Date, nullable=False)


class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grades_student_id = db.Column(db.Integer) # foreign keys !!!!!!!!!!!!!!
    grades_tutor_id = db.Column(db.Integer)
    grades_enrol_id = db.Column(db.Integer)
    academic_year = db.Column(db.Date, nullable=False)
    ca1_score = db.Column(db.Integer, nullable=False)
    ca2_score = db.Column(db.Integer, nullable=False)
    exam_score = db.Column(db.Integer, nullable=False)


# db.drop_all()
# db.create_all()

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