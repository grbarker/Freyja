from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Employee


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')



class EmployeeRegistrationForm(FlaskForm):
    employee_id = StringField('Employee ID', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    firstname = StringField('First name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_employee_id(self, employee_id):
        employee = Employee.query.filter_by(employeeID=employee_id.data).first()
        if employee is not None:
            raise ValidationError('Please use a different ID number.')

    def validate_name(self, lastname, firstname):
        employee = Employee.query.filter_by(lastname=lastname.data, firstname=firstname.data).first()
        if employee is not None:
            raise ValidationError('This name is already in use. Please use a different first and last name.')

##Pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

##from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')