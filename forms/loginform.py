from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    emaill = EmailField(validators=[DataRequired()])
    passwordl = PasswordField(validators=[DataRequired()])
    submitl = SubmitField('Log In')

    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_again = PasswordField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    submit = SubmitField('Get Started')
