from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_required,login_user,logout_user,current_user
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap5
from form import *
app = Flask(__name__)
bcrypt = Bcrypt(app)
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "iwwjhweugfjujfhigeru83y28rhkm"
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
class Users(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    email: Mapped[str] = mapped_column(String(150),unique=True,nullable=False)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    password : Mapped[str] = mapped_column(String(200),nullable=False)
    tel_no : Mapped[int] = mapped_column(Integer,nullable=True)

class Birthday(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    date: Mapped[str] = mapped_column(String,nullable=False)
    user_id: Mapped[int] = mapped_column(String,nullable=False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    user = Users.query.where(Users.id == user_id).scalar()
    if user:
        return user
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('about-us.html')

@app.route('/register')
def signup():
    form = RegisterForm()
    name = form.password.data
    password = form.password.data
    email = form.email.data
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(password)
    return render_template('register.html',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)
@app.route('/user-page')
def user_page():
    return render_template('user-page.html')
if __name__ == '__main__':
    app.run(debug=True)