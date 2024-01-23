from flask import render_template, url_for, request, flash, redirect, Blueprint, abort

login_route = Blueprint('login_route', __name__)

# Your existing routes
@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the registration logic here
        # For simplicity, we'll just redirect back to the login page.
        return redirect(url_for('registration_route.register'))

    return render_template('user_login.html')