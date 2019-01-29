##Form code initially taken from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
##then altered as necessary to fit the needs of the project
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Employee


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

##Next two pulled from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class SortForm(FlaskForm):
    sort_type = SelectField('Sort', coerce=int)
    submit = SubmitField('Sort')
