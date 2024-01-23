from flask import render_template, url_for, request, flash, redirect, Blueprint, abort

registration_route = Blueprint('registration_route', __name__)

# Your existing routes
@registration_route.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle the registration logic here
        # For simplicity, we'll just redirect back to the login page.
        return redirect(url_for('login_route.login'))

    return render_template('user_registration.html')