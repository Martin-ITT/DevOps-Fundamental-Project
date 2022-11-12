from application import db

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrolments = db.relationship('Enrolments', backref='students') # FK one to many Enrolments
    student_fname = db.Column(db.String(30), nullable=False)
    student_lname = db.Column(db.String(30), nullable=False)
    student_address1 = db.Column(db.String(50), nullable=False)
    student_address2 = db.Column(db.String(50), nullable=False)
    student_city = db.Column(db.String(30), nullable=False)
    student_county = db.Column(db.String(30), nullable=False)
    student_phone = db.Column(db.Integer, nullable=False)
    student_DOB = db.Column(db.Date, nullable=False)
    student_email = db.Column(db.String(50), nullable=False)
    student_password_ff = db.Column(db.String(150), nullable=False)
    authority_lvl = db.Column(db.Integer, nullable=False)


class Tutors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t_modules = db.relationship('Modules', backref='tutors') # FK ref Modules
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
    academic_year = db.Column(db.Date, nullable=False)
    ca1_score = db.Column(db.Integer)
    ca2_score = db.Column(db.Integer)
    exam_score = db.Column(db.Integer)
