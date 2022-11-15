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
    student_address1 = 'address1_' + str(i),
    student_address2 = 'address2_' + str(i),
    student_city = 'city' + str(i),
    student_county = 'county' + str(i),
    student_phone =  str(random.randint(871111111, 879999999)),
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
    tutor_phone =  str(random.randint(871111111, 879999999)),
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


for i in range(1,12):
    for x in range (1, random.randint(3,5)):
        enrolment = Enrolments(enrol_student_id = i,
        enrol_module_id = x,
        academic_year = date(year=2022, month=9, day=1),
        ca1_score = random.randint(1,100),
        ca2_score = random.randint(1,100),
        exam_score = random.randint(1,100))
        db.session.add(enrolment)


student = Students(student_fname = 'John',
    student_lname = 'Doe',
    student_address1 = '1 Main Street',
    student_address2 = '',
    student_city = 'Johnstown' + str(i),
    student_county = 'Leitrim',
    student_phone =  str(871234567),
    student_DOB = date(year = random.randint(1960, 2004), month=random.randint(1, 12), day=random.randint(1, 28)),
    student_email = 'john@john.com',
    student_password_ff = 'pbkdf2:sha512:52000$JwTTeoU3pUAIvApF$7d9fd2c5abe989653c4f09dce2b1252ddcbc1a4eb37041d3c26ee0b3a49c6c60e7a0a85908abfbab900a2e27a1f06dd3590d1e76aa9639e49f569502bc92be5f',
    authority_lvl = 0)

db.session.add(student)


tutor = Tutors(tutor_fname = 'admin',
    tutor_lname = 'admin',
    tutor_address1 = 'address1 ',
    tutor_address2 = 'address2 ',
    tutor_city = 'city',
    tutor_county = 'county',
    tutor_phone =  "0871111111",
    tutor_DOB = date(year = 1960, month=1, day=1),
    tutor_email = 'admin@admin.com', # peter5555
    tutor_password_ff = 'pbkdf2:sha512:52000$JwTTeoU3pUAIvApF$7d9fd2c5abe989653c4f09dce2b1252ddcbc1a4eb37041d3c26ee0b3a49c6c60e7a0a85908abfbab900a2e27a1f06dd3590d1e76aa9639e49f569502bc92be5f',
    authority_lvl = 2)

db.session.add(tutor)

db.session.commit()