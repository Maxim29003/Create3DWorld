from flask import render_template, request, redirect, url_for
from app import app
from app.forms import RegisterForm, LoginForm


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

        print('Name {0}, Email {1}, Password {2}'.format(name, email,password))
    return render_template('register.html', form = register_form)


@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        print('Email {0}, Password {1}'.format(email,password))
    return render_template('login.html', form = login_form)