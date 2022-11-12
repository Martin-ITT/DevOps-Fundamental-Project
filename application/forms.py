from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo, DataRequired, Regexp)

# user registration forms
class RegistrationForm(FlaskForm):
    '''
    user_name = StringField('user_name', validators=[DataRequired(), Length(
        min=5, max=15, message='Name must be between \
            %(min)d and %(max)d characters long')])
    '''
    user_password = PasswordField(
        'user_password', validators=[DataRequired(), Length(
            min=8, max=20, message='Password must be between  %(min)d and \
                %(max)d characters long.')])
    '''
    check_password = PasswordField(
        'check_password', validators=[EqualTo(
            'user_password', message="Passwords don't match")])
    '''
    user_email = StringField(
        'user_email', validators=[InputRequired(), Email(), Length(max=40), Regexp('^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', message="Invalid characters in email address.")])