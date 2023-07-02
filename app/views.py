from flask import render_template, request, redirect, url_for
from app import app, login_manager,db
from app.forms import RegisterForm, LoginForm
from flask_login import UserMixin, login_user, logout_user, login_required
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        name = register_form.name.data
        email = register_form.email.data
        password = register_form.password.data
        user = User(name = name, email = email,password = password)
        db.session.add(user)
        db.session.commit()
        print('Name {0}, Email {1}, Password {2}'.format(name, email,password))
        return redirect(url_for('login'))
    return render_template('register.html', form = register_form)


@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email = email).first()
        if user and user.password == password:
            login_user(user)
            print('Email {0}, Password {1}'.format(email,password))
            return redirect(url_for('home'))
        return 'Пароль не верный '
        
    return render_template('login.html', form = login_form)


@app.route('/home')
@login_required
def home():
    return 'Hi'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))