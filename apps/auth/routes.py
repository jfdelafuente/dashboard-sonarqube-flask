from flask import render_template, url_for, redirect, request
from apps.auth.forms import LoginForm, CreateAccountForm
from apps.auth import auth
from apps.auth.util import verify_pass

@auth.route("/")
def route_default():
    return redirect(url_for('auth.login'))

@auth.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        # read form data
        username = request.form['username']
        password = request.form['password']
        
        # Check the password
        if verify_pass(password, "HOLA"):
            return redirect(url_for('auth.route_default'))
        
    return render_template('auth/login.html',
                               msg='Wrong user or password',
                               form=login_form)

@auth.route("/register")
def register():
    return render_template('auth/register.html')

@auth.route("/password")
def password():
    return render_template('auth/password.html')

