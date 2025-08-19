from flask_wtf import FlaskForm
from wtforms import StringField , EmailField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired ,Length , Email , Regexp ,EqualTo , ValidationError
from VAG.models import User
class RegistrationForm(FlaskForm):
    fname = StringField('Frist Name',validators=[DataRequired(), Length(min=2 , max=25)])
    lname = StringField('Last Name',validators=[DataRequired(), Length(min=2 , max=25)])
    username = StringField('Username',validators=[DataRequired(), Length(min=2 , max=25)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$")])
    confirm_password = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already exists! Please chosse a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email already exists! Please chosse a different one')


class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')