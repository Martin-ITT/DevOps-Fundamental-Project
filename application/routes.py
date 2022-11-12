from application import app, db
from flask import render_template, flash, redirect, url_for, session
from application.models import Students, Tutors, Modules, Enrolments
from application.forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # refer to registration form
    form = RegistrationForm()
    # print(form.user_email)

    # POST method
    if form.validate_on_submit():
        
        email = form.user_email.data
        password = form.user_password.data

        # check if email exists
        existing_email = Students.query.filter_by(student_email=email).all()
      
        # if email exists
        if existing_email:
            for email in existing_email:
                print(email.student_city)
            flash("Email already registered. Please contact registrar office.")
            return redirect(url_for('register'))
        
        else:
            student = Students(student_fname = 'Please update your name',
            student_lname = 'Please update your name',
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
            print(generate_password_hash(
                form.user_password.data,
                method='pbkdf2:sha512:52000',
                salt_length=16))
        

        # user cookie session
        session["user"] = form.user_email.data.lower()
        flash("User registered succesfully")
        # flash("cookie: {}".format(session['user']))
        
        # return redirect(url_for('profile', username=session['user']))
        return redirect(url_for('register'))

    students = Students.query.filter_by(student_fname="fname1").all()
    return render_template("register.html", form=form, students=students)
