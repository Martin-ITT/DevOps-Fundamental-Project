from application import app, db
from flask import render_template, flash, redirect, url_for, session
from application.models import Students, Tutors, Modules, Enrolments
from application.forms import RegistrationForm, LoginForm
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

        # check if email exists
        existing_email = Students.query.filter_by(student_email=email).all()

        # if email exists
        if existing_email:
            '''
            for email in existing_email:
                print(email.student_city)
            '''
            flash("Email already registered. Please contact registrar office.")
            return redirect(url_for('register'))

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

            # user cookie session
            session["user_email"] = form.user_email.data.lower()
            flash("User registered succesfully")
            # flash("cookie: {}".format(session['user']))

            # return redirect(url_for('profile', username=session['user']))
            return redirect(url_for('register'))

    students = Students.query.filter_by(student_fname="fname1").all()
    return render_template("register.html", form=form, students=students)


# user login route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # on submit check if user exist
    if form.validate_on_submit():
        email = form.user_login_email.data
        # check if email exists
        student = Students.query.filter_by(student_email=email).all()
        
        get_email_fromDB = ""
        get_fname_fromDB = ""
        for item in student:
            get_email_fromDB = item.student_password_ff
            get_fname_fromDB = item.student_fname
        
        if student:
            # check if password match
            if check_password_hash(get_email_fromDB,
                                   form.user_login_password.data):

                    session["user_email"] = form.user_login_email.data.lower()
                    flash("Welcome, {}".format(get_fname_fromDB))
                    # flash("cookie: {}".format(session['user']))
                    return redirect(
                        url_for('profile', useremail=session['user_email']))

            else:
                # password dont match
                flash("Incorrect login details")
                return redirect(url_for('login'))

        else:
            # incorrect user email
            flash("Incorrect login details")
            return redirect(url_for('login'))

    return render_template("login.html", form=form)


# user profile route
@app.route("/profile/<useremail>", methods=["GET", "POST"])
def profile(useremail):
    
    # only render if session cookie exist
    if session['user_email']:
        student = Students.query.filter_by(student_email=session["user_email"]).all()
        '''
        # find user name in mongo using session cookie. [only user_name]
        username = mongo.db.users.find_one(
            {"user_name": session["user"]})["user_name"]
        '''
        # first to be retrieved on html, second from previous line
        return render_template("profile.html", student = student)
    
    return redirect(url_for("login"))


# user logout route
@app.route("/logout")
def logout():
    # remove user from cookie session
    session.pop("user_email")
    flash("You have been logged out")
    return redirect(url_for("login"))
