from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,EmailField,DateField
from wtforms.validators import DataRequired,Length,Email

class RegisterForm(FlaskForm):
    name= StringField('User Name:',[DataRequired(),Length(20)])
    email=StringField('User Email',[DataRequired()])
    password = StringField('Password',[DataRequired()])
    birthday = DateField('Your Birthday',[DataRequired()])
    submit = SubmitField('Register!')