from application import db
from datetime import date
import random
from application.models import Students, Tutors, Enrolments, Modules

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
    m_tutor_id = random.randint(1, 5),
    description = 'module description ' + str(i))

    db.session.add(module)


for i in range(1,11):
    for x in range (1, random.randint(3,5)):
        enrolment = Enrolments(enrol_student_id = i,
        enrol_module_id = x,
        academic_year = date(year=2022, month=9, day=1))

        db.session.add(enrolment)


db.session.commit()