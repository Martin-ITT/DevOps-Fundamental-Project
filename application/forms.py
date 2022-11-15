# from werkzeug.security import generate_password_hash, check_password_hash
from application.models import Tutors
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField, FormField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import validators
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo, DataRequired, Regexp)

# user registration forms
class RegistrationForm(FlaskForm):
    
    user_fname = StringField('user_fname', validators=[DataRequired(), Length(
        min=2, max=30, message='Name must be between \
            %(min)d and %(max)d characters long')])
    user_lname = StringField('user_lname', validators=[DataRequired(), Length(
            min=2, max=30, message='Name must be between \
                %(min)d and %(max)d characters long')])
    user_password = PasswordField(
        'user_password', validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between  %(min)d and \
                %(max)d characters long.')])
    check_password = PasswordField(
        'check_password', validators=[EqualTo(
            'user_password', message="Passwords don't match")])
    user_email = StringField(
        'user_email', validators=[InputRequired(), Email(), Length(max=40), Regexp(
            '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$',
            message="Invalid characters in email address.")])

# user login form
class LoginForm(FlaskForm):
    user_login_email = StringField(
        'user_login_email', validators=[DataRequired(), Length(
            max=40, message='Email must be maximum of \
                %(max)d characters long')])
    user_login_password = PasswordField(
        'user_login_password', validators=[DataRequired()])

class StudentForm(FlaskForm):
    # enrolments ##############################################################################
    # SelectMultipleField(default field arguments, choices=[], coerce=unicode, option_widget=None)
    # FormField(form_class, default field arguments, separator='-')
    '''
    class TelephoneForm(Form):
        country_code = IntegerField('Country Code', [validators.required()])
        area_code    = IntegerField('Area Code/Exchange', [validators.required()])
        number       = StringField('Number')

    class ContactForm(Form):
        first_name   = StringField()
        last_name    = StringField()
        mobile_phone = FormField(TelephoneForm)
        office_phone = FormField(TelephoneForm)
    '''
    student_fname = StringField('student_fname', validators=[DataRequired(), Length(
        min=2, max=30, message='Name must be between \
            %(min)d and %(max)d characters long')])
    student_lname = StringField('student_lname', validators=[DataRequired(), Length(
        min=2, max=30, message='Name must be between \
            %(min)d and %(max)d characters long')])
    student_address1 = StringField('student_address1', validators=[Length(
        min=2, max=50, message='Address must be between \
            %(min)d and %(max)d characters long')])
    student_address2 = StringField('student_address2', validators=[Length(
        min=2, max=50, message='Address must be between \
            %(min)d and %(max)d characters long')])
    student_city = StringField('student_city', validators=[Length(
        min=2, max=30, message='City must be between \
            %(min)d and %(max)d characters long')])
    student_county = StringField('student_county', validators=[Length(
        min=4, max=30, message='County must be between \
            %(min)d and %(max)d characters long')])
    student_phone = StringField('student_phone', validators=[Length(
        min=8, max=20, message='Phone number must be  \
            %(max)d characters long'), Regexp('^[+-]?[0-9]$',
            message="Invalid characters in phone number.")])
    student_DOB = DateField('student_DOB')
    student_email = StringField('student_email', validators=[Length(
        max=50, message='Email must be between \
            %(min)d and %(max)d characters long')])
    student_password_ff = PasswordField('user_password',
        validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between  %(min)d and \
            %(max)d characters long.')])
    authority_lvl = IntegerField('authority_lvl', validators=[Length(max=10)])


class TutorForm(FlaskForm):
    # enrolments ##############################################################################
    # SelectMultipleField(default field arguments, choices=[], coerce=unicode, option_widget=None)
    # FormField(form_class, default field arguments, separator='-')
    '''
    class TelephoneForm(Form):
        country_code = IntegerField('Country Code', [validators.required()])
        area_code    = IntegerField('Area Code/Exchange', [validators.required()])
        number       = StringField('Number')

    class ContactForm(Form):
        first_name   = StringField()
        last_name    = StringField()
        mobile_phone = FormField(TelephoneForm)
        office_phone = FormField(TelephoneForm)
    '''
    tutor_fname = StringField('tutor_fname', validators=[DataRequired(), Length(
        min=2, max=30, message='Name must be between \
            %(min)d and %(max)d characters long')])
    tutor_lname = StringField('tutor_lname', validators=[DataRequired(), Length(
        min=2, max=30, message='Name must be between \
            %(min)d and %(max)d characters long')])
    tutor_address1 = StringField('tutor_address1', validators=[Length(
        min=2, max=50, message='Address must be between \
            %(min)d and %(max)d characters long')])
    tutor_address2 = StringField('tutor_address2', validators=[Length(
        min=2, max=50, message='Address must be between \
            %(min)d and %(max)d characters long')])
    tutor_city = StringField('tutor_city', validators=[Length(
        min=2, max=30, message='City must be between \
            %(min)d and %(max)d characters long')])
    tutor_county = StringField('tutor_county', validators=[Length(
        min=4, max=30, message='County must be between \
            %(min)d and %(max)d characters long')])
    tutor_phone = StringField('tutor_phone', validators=[Length(
        min=8, max=20, message='Phone number must be  \
            %(max)d characters long'), Regexp('^[+-]?[0-9]$',
            message="Invalid characters in phone number.")])
    tutor_DOB = DateField('tutor_DOB')
    tutor_email = StringField('tutor_email', validators=[Length(
        max=50, message='Email must be between \
            %(min)d and %(max)d characters long')])
    tutor_password_ff = PasswordField('user_password',
        validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between  %(min)d and \
            %(max)d characters long.')])
    authority_lvl = IntegerField('authority_lvl', validators=[Length(max=10)])


def select_tutor():
    return Tutors.query


class ModulesForm(FlaskForm):
    module_name = StringField('Module_name')
    description = StringField('Module_description')
    enrolments = FormField(StudentForm, 'enrolments')
    tutors = QuerySelectField(query_factory=select_tutor, validators=[DataRequired()])
