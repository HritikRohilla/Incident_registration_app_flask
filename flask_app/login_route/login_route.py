from flask_app.models import User
from flask_app.common_functiom import verify_password
from flask import render_template, url_for, request, flash, redirect, Blueprint, session

login_route = Blueprint('login_route', __name__)

@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the entered username and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()

        if user and verify_password(password, user.password):
            # Password is correct, log the user in
            flash('Login successful!')

            # You can store user information in the session for future use
            session['user_id'] = user.id
            session['username'] = user.username

            # Redirect to a register Incident or another page after successful login
            # TODO: route will change
            return redirect(url_for('login_route.login'))

        else:
            # Incorrect username or password
            flash('Wrong credential. Please try again.')

    return render_template('user_login.html')