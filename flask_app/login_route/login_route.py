from flask_app.models import User
from flask_app.common_functiom import verify_password
from flask_app.decorator.decorator import already_loggedin
from flask import render_template, url_for, request, flash, redirect, Blueprint, session

login_route = Blueprint('login_route', __name__)

@login_route.route('/', methods=['GET', 'POST'])
@already_loggedin
def login():
    if request.method == 'POST':
        # Get the entered username and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()

        if user and verify_password(password, user.password):

            # You can store user information in the session for future use
            session['user_id'] = user.id
            session['username'] = user.username

            # Redirect to a register Incident after successful login
            return redirect(url_for('incident_route.home'))

        else:
            # Incorrect username or password
            flash('Wrong credential. Please try again.')

    return render_template('user_login.html')


@login_route.route('/logout', methods=['GET'])
def logout():
    session.clear()

    return redirect(url_for('login_route.login'))