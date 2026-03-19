from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,DateField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from flask_ckeditor import CKEditorField

class RegisterForm(FlaskForm):
    name= StringField('User Name:',[DataRequired(),Length(max=50,message='Sorry, this name is too long.')])
    email=StringField('User Email',[DataRequired(),Email('Invalid Email')])
    password = PasswordField('Password',[DataRequired(),Length(min=8,message='Sorry, your password must be at 8 characters long.')])
    birthday = DateField('Your Birthday',[DataRequired()])
    submit = SubmitField('Register!')

class LoginForm(FlaskForm):
    email = StringField('User Email', [DataRequired(),Email('Invalid Email')])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login!')

class ContactForm(FlaskForm):
    name = StringField('Name:',[DataRequired(),Length(max=50,message='Sorry, this name is too long.')])
    email = EmailField('Email:',[DataRequired()])
    message = CKEditorField('Message',[DataRequired])
    send = SubmitField('Send!')