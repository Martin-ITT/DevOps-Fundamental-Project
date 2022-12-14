from application import app, db
from flask import render_template, request, flash, redirect, url_for, session
from application.models import Students, Tutors, Modules, Enrolments
from application.forms import (
    RegistrationForm, LoginForm, StudentForm, TutorForm,
        ModulesForm, AddModulesForm, GradesForm, EnrolmentForm)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from flask_sqlalchemy import SQLAlchemy

# index page route
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


# student registration
@app.route("/student_register", methods=["GET", "POST"])
def student_register():
    # refer to registration form
    form = RegistrationForm()

    # POST method
    if form.validate_on_submit():

        email = form.user_email.data

        # check if email exists
        existing_email = Students.query.filter_by(student_email=email).first()

        # if email exists
        if existing_email:

            flash("Email already registered. Please contact registrar office.")
            return redirect(url_for('student_register'))

        else:
            student = Students(student_fname = form.user_fname.data,
            student_lname = form.user_lname.data,
            student_address1 = 'Please update your address',
            student_address2 = 'Please update your address',
            student_city = 'Please update your address',
            student_county = 'Please update your address',
            student_phone =  871111111,
            student_DOB = date(year = 2000, month=1, day=1),
            student_email = email,
            student_password_ff = generate_password_hash(
                form.user_password.data,
                method='pbkdf2:sha512:52000',
                salt_length=16),
            authority_lvl = 0)

            db.session.add(student)
            db.session.commit()

            # f = open("mynew.txt", "w")
            # f.write(student.student_password_ff)
            # f.close()

            # user cookie session
            session["user_email"] = form.user_email.data.lower()
            flash("User registered succesfully")
            # flash("cookie: {}".format(session['user']))

            # return redirect(url_for('profile', username=session['user']))
            return redirect(url_for('profile', user_email=session['user_email']))

    students = Students.query.filter_by(student_fname="fname1").all()
    return render_template("student_register.html", form=form, students=students)


# tutor registration
@app.route("/tutor_register", methods=["GET", "POST"])
def tutor_register():
    tutors = Tutors.query.filter_by(tutor_fname="fname1").all()
    # refer to registration form
    form = RegistrationForm()

    # POST method
    if form.validate_on_submit():

        email = form.user_email.data

        # check if email exists
        existing_email = Tutors.query.filter_by(tutor_email=email).all()

        # if email exists
        if existing_email:

            flash("Email already registered. Please contact registrar office.")
            return redirect(url_for('tutor_register'))

        else:
            tutor = Tutors(tutor_fname = form.user_fname.data,
            tutor_lname = form.user_lname.data,
            tutor_address1 = 'Please update your address',
            tutor_address2 = 'Please update your address',
            tutor_city = 'Please update your address',
            tutor_county = 'Please update your address',
            tutor_phone =  871111111,
            tutor_DOB = date(year = 2000, month=1, day=1),
            tutor_email = email,
            tutor_password_ff = generate_password_hash(
                form.user_password.data,
                method='pbkdf2:sha512:52000',
                salt_length=16),
            authority_lvl = 0)

            db.session.add(tutor)
            db.session.commit()

            # user cookie session
            session["user_email"] = form.user_email.data.lower()
            flash("User registered succesfully")
            # flash("cookie: {}".format(session['user']))

            # return redirect(url_for('profile', username=session['user']))
            return redirect(url_for('tutor_register'))
    
    return render_template("tutor_register.html", form=form, tutors=tutors)


# student login route
@app.route("/student_login", methods=["GET", "POST"])
def student_login():
    form = LoginForm()

    # on submit check if user exist
    if form.validate_on_submit():
        email = form.user_login_email.data
        # check if email exists
        student = Students.query.filter_by(student_email=email).first()
        
        if student:
            # check if password match
            if check_password_hash(student.student_password_ff,
                                   form.user_login_password.data):

                    session["user_email"] = form.user_login_email.data.lower()
                    flash("Welcome, {}".format(student.student_fname))
                    return redirect(
                        url_for('profile', user_email=session['user_email'], student=student))

            else:
                # password dont match
                flash("Incorrect login details")
                return redirect(url_for('student_login'))

        else:
            # incorrect user email
            flash("Incorrect login details")
            return redirect(url_for('student_login'))

    return render_template("student_login.html", form=form)


# tutor login route
@app.route("/tutor_login", methods=["GET", "POST"])
def tutor_login():
    form = LoginForm()

    # on submit check if user exist
    if form.validate_on_submit():
        email = form.user_login_email.data
        # check if email exists
        tutor = Tutors.query.filter_by(tutor_email=email).first()

        if tutor:
            # check if password match
            if check_password_hash(tutor.tutor_password_ff, form.user_login_password.data):
                session["user_email"] = form.user_login_email.data.lower()
                flash("Welcome, {}".format(tutor.tutor_fname))
                return redirect(
                    url_for('tutor_profile', user_email=session['user_email'], tutor=tutor))

            else:
                # password dont match
                flash("Incorrect login details")
                return redirect(url_for('tutor_login'))

        else:
            # incorrect user email
            flash("Incorrect login details")
            return redirect(url_for('tutor_login'))

    return render_template("tutor_login.html", form=form)


# student profile route
@app.route("/profile", methods=["GET", "POST"])
def profile():
   
    # only render if session cookie exist
    if session['user_email']:
        student = Students.query.filter_by(student_email=session["user_email"]).first()

        return render_template("profile.html", student=student)
    
    return redirect(url_for("login"))


# tutor profile route
@app.route("/tutor_profile", methods=["GET", "POST"])
def tutor_profile():
   
    # only render if session cookie exist
    if session['user_email']:
        tutor = Tutors.query.filter_by(tutor_email=session["user_email"]).first()

        return render_template("tutor_profile.html", tutor=tutor)
    
    return redirect(url_for("tutor_login"))


# user logout route
@app.route("/logout")
def logout():
    # remove user from cookie session
    session.pop("user_email")
    flash("You have been logged out")
    return redirect(url_for("home"))


# update student profile
@app.route("/update_student_profile/<int:student_id>", methods=["GET", "POST"])
def update_student_profile(student_id):
    if session['user_email']:

        form = StudentForm()
        student = Students.query.filter_by(id=student_id).first()
        print(student)

        # POST method
        if request.method == "POST":
        # if form.validate_on_submit():

            student.student_fname = form.student_fname.data
            student.student_lname = form.student_lname.data
            student.student_address1 = form.student_address1.data
            student.student_address2 = form.student_address2.data
            student.student_city = form.student_city.data
            student.student_county = form.student_county.data
            student.student_phone =  form.student_phone.data
            student.student_DOB = form.student_DOB.data
            student.student_email = form.student_email.data

            # update student in database
            db.session.commit()
            flash("Record updated")

            if session['user_email'] == "admin@admin.com":
                return redirect(url_for('student_management'))

            return redirect(url_for('profile', user_email=session['user_email']))

    return render_template("update_student_profile.html", form=form, student=student)


# update tutor profile
@app.route("/update_tutor_profile/<int:tutor_id>", methods=["GET", "POST"])
def update_tutor_profile(tutor_id):
    if session['user_email']:

        form = TutorForm()
        tutor = Tutors.query.filter_by(id=tutor_id).first()
        
        # POST method
        if request.method == "POST":
        # if form.validate_on_submit():

            tutor.tutor_fname = form.tutor_fname.data
            tutor.tutor_lname = form.tutor_lname.data
            tutor.tutor_address1 = form.tutor_address1.data
            tutor.tutor_address2 = form.tutor_address2.data
            tutor.tutor_city = form.tutor_city.data
            tutor.tutor_county = form.tutor_county.data
            tutor.tutor_phone =  form.tutor_phone.data
            tutor.tutor_DOB = form.tutor_DOB.data
            tutor.tutor_email = form.tutor_email.data

            # update tutor in database
            db.session.commit()
            flash("Record updated")

            if session['user_email'] == "admin@admin.com":
                return redirect(url_for('tutor_management'))

            return redirect(url_for('tutor_profile', user_email=session['user_email']))

    return render_template("update_tutor_profile.html", form=form, tutor=tutor)

# student management
@app.route("/student_ management")
def student_management():
    if session['user_email']:
        
        students = Students.query.all()
        # students = Students.query.paginate(per_page=5, error_out=True)
    
        return render_template("student_management.html", students=students)

    return redirect(url_for('home'))


# delete student record
@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):
    if session['user_email'] == "admin@admin.com":
        
        student = Students.query.filter_by(id=student_id).first()
        db.session.delete(student)
        db.session.commit()
        students = Students.query.all()
        flash("Record deleted!")
    
        return render_template("student_management.html", students=students)

    return redirect(url_for('home'))


# admin_add_student
@app.route("/admin_add_student", methods=["GET", "POST"])
def admin_add_student():
    if session['user_email'] == "admin@admin.com":
        # refer to registration form
        form = RegistrationForm()

        # POST method
        if form.validate_on_submit():

            email = form.user_email.data

            # check if email exists
            existing_email = Students.query.filter_by(student_email=email).first()

            # if email exists
            if existing_email:

                flash("Email already registered")
                return redirect(url_for('admin_add_student'))

            else:
                student = Students(student_fname = form.user_fname.data,
                student_lname = form.user_lname.data,
                student_address1 = 'Please update your address',
                student_address2 = 'Please update your address',
                student_city = 'Please update your address',
                student_county = 'Please update your address',
                student_phone =  871111111,
                student_DOB = date(year = 2000, month=1, day=1),
                student_email = email,
                student_password_ff = generate_password_hash(
                    form.user_password.data,
                    method='pbkdf2:sha512:52000',
                    salt_length=16),
                authority_lvl = 0)

                db.session.add(student)
                db.session.commit()

                flash("User registered succesfully")
             
                return redirect(url_for('student_management'))

        # students = Students.query.filter_by(student_fname="fname1").all()
        return render_template("student_register_admin.html", form=form)

    return redirect(url_for('home'))


# admin_add_tutor
@app.route("/admin_add_tutor", methods=["GET", "POST"])
def admin_add_tutor():
    if session['user_email'] == "admin@admin.com":
        # refer to registration form
        form = RegistrationForm()

        # POST method
        if form.validate_on_submit():

            email = form.user_email.data

            # check if email exists
            existing_email = Tutors.query.filter_by(tutor_email=email).first()

            # if email exists
            if existing_email:

                flash("Email already registered")
                return redirect(url_for('admin_add_tutor'))

            else:
                tutor = Tutors(tutor_fname = form.user_fname.data,
                tutor_lname = form.user_lname.data,
                tutor_address1 = 'Please update your address',
                tutor_address2 = 'Please update your address',
                tutor_city = 'Please update your address',
                tutor_county = 'Please update your address',
                tutor_phone =  871111111,
                tutor_DOB = date(year = 2000, month=1, day=1),
                tutor_email = email,
                tutor_password_ff = generate_password_hash(
                    form.user_password.data,
                    method='pbkdf2:sha512:52000',
                    salt_length=16),
                authority_lvl = 0)

                db.session.add(tutor)
                db.session.commit()

                flash("User registered succesfully")
             
                return redirect(url_for('tutor_management'))

        return render_template("tutor_register_admin.html", form=form)

    return redirect(url_for('home'))


# tutor management
@app.route("/tutor_ management")
def tutor_management():
    if session['user_email']:
        
        tutors = Tutors.query.all()
        return render_template("tutor_management.html", tutors=tutors)

    return redirect(url_for('home'))


# delete tutor record
@app.route("/delete_tutor/<int:tutor_id>")
def delete_tutor(tutor_id):
    if session['user_email'] == "admin@admin.com":
        
        tutor = Tutors.query.filter_by(id=tutor_id).first()
        db.session.delete(tutor)
        db.session.commit()
        tutors = Tutors.query.all()
        flash("Record deleted!")
    
        return render_template("tutor_management.html", tutors=tutors)

    return redirect(url_for('home'))


# modules management
@app.route("/modules_management")
def modules_management():
    if session['user_email'] == "admin@admin.com":
        
        modules = Modules.query.all()
        f = open("mynew.txt", "w")
        for module in modules:
            f.write("name: " + module.module_name)
            f.write(" - tutor: " + str(module.m_tutor_id))
            f.write(" - enrolments: " + str(module.enrolments) + "\n")
        f.close()
            
        return render_template("modules_management.html", modules=modules)

    return redirect(url_for('home'))


# admin_add_module
@app.route("/admin_add_module", methods=["GET", "POST"])
def admin_add_module():
    if session['user_email'] == "admin@admin.com":
        form = AddModulesForm()

        # POST method
        if request.method == "POST":
            
            module = Modules(module_name = form.module_name.data,
                description = form.description.data,
                m_tutor_id = form.tutors.data)

            db.session.add(module)
            db.session.commit()

            flash("Record added!")
            return(redirect('modules_management'))
       
        return render_template("module_register_admin.html", form=form)

    return redirect(url_for('home'))


# update module
@app.route("/update_module/<int:module_id>", methods=["GET", "POST"])
def update_module(module_id):
    if session['user_email'] == "admin@admin.com":

        form = ModulesForm()
        module = Modules.query.filter_by(id=module_id).first()
        
        # POST method
        if request.method == "POST":
        # if form.validate_on_submit():

            module.module_name = form.module_name.data
            module.description = form.description.data
            module.m_tutor_id = form.tutors.data.id

            # update tutor in database
            db.session.commit()
            flash("Record updated")

            return redirect(url_for('modules_management'))

            # return redirect(url_for('profile', user_email=session['user_email']))

    return render_template("update_modules.html", form=form, module=module)


# delete module
@app.route("/delete_module/<int:module_id>")
def delete_module(module_id):
    if session['user_email'] == "admin@admin.com":
        
        module = Modules.query.filter_by(id=module_id).first()
        db.session.delete(module)
        db.session.commit()
        modules = Modules.query.all()
        flash("Record deleted!")
    
        return render_template("modules_management.html", modules=modules)

    return redirect(url_for('home'))


# student can check grades
@app.route("/student_grades_check/<int:student_id>")
def student_grades_check(student_id):
    if session['user_email']:

        enrolments = Enrolments.query.filter_by(enrol_student_id=student_id).all()
        
    return render_template("student_grades.html", enrolments=enrolments)


# tutor marks a student
@app.route("/tutor_grades/<int:tutor_id>")
def tutor_grades(tutor_id):
    # need to add && auth level == 1
    if session['user_email']:

        enrolments = Enrolments.query\
            .join(Modules, Modules.id == Enrolments.enrol_module_id)\
                .add_columns(Modules.module_name, Modules.m_tutor_id)\
                    .join(Students, Students.id == Enrolments.enrol_student_id)\
                        .add_columns(Students.student_lname)\
                            .join(Tutors, Modules.m_tutor_id == Tutors.id )\
                                .add_columns(Tutors.tutor_lname)\
                                    .filter(Modules.m_tutor_id == tutor_id).all()
        
        
    return render_template("tutor_grades.html", enrolments=enrolments)


# tutor can update grades here
@app.route("/tutor_update_grades/<int:enrolment_id>", methods=["GET", "POST"])
def tutor_update_grades(enrolment_id):
    if session['user_email']:

        form = GradesForm()
        enrolment = Enrolments.query.filter_by(id=enrolment_id).first()
        
        # POST method
        if request.method == "POST":
        # if form.validate_on_submit():

            enrolment.ca1_score = form.ca1.data
            enrolment.ca2_score = form.ca2.data
            enrolment.exam_score = form.exam.data

            # update tutor in database
            db.session.commit()
            flash("Record updated")

            return redirect(url_for('tutor_profile', user_email=session['user_email']))

            # return redirect(url_for('profile', user_email=session['user_email']))

        return render_template("update_grades.html", form=form, enrolment=enrolment)


#enrolment management
@app.route("/enrolment_management/", methods=["GET", "POST"])
def enrolment_management():
    if session['user_email']:

        form = EnrolmentForm()
        # enrolment = Enrolments.query.filter_by(id=enrolment_id).first()
        
        # POST method
        if request.method == "POST":
        # if form.validate_on_submit():
            
            enrolment = Enrolments(enrol_student_id = form.enrol_student_id.data,
            enrol_module_id = form.enrol_module_id.data,
            academic_year = date(year=2022, month=9, day=1))

            db.session.add(enrolment)
            db.session.commit()

            
            # update tutor in database
            # db.session.commit()
            flash("Record added")

            return redirect(url_for('enrolment_management'))

            # return redirect(url_for('profile', user_email=session['user_email']))

        return render_template("enrolment_management.html", form=form)

# error handling
@app.errorhandler(404)
def page_not_found(err):
        error_msg = err
        flash("This is weird. It is not here!")
        return render_template("error.html", error_msg=error_msg)


@app.errorhandler(500)
def server_error(err):
    error_msg = err
    flash("Something's not quite right.")
    return render_template("error.html", error_msg=error_msg)