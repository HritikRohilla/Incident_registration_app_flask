from flask_app.common_functiom import hash_password
from flask_app.models import User, db
from flask import render_template, url_for, request, flash, redirect, Blueprint

recover_password = Blueprint('recover_password', __name__)


@recover_password.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':

        email = request.form.get('email')
        return redirect(url_for('recover_password.reset_password', email=email))

    return render_template('forgot_password.html')

@recover_password.route('/reset_password/<email>', methods=['GET', 'POST'])
def reset_password(email):
    if request.method == 'POST':
        # Get the passwords from the form
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password == confirm_password:
            # Hashing password
            hashed_password = hash_password(password)

            user = User.query.filter_by(email=email).first()

            if user:
                user.password = hashed_password
                db.session.commit()

                flash('Password reset successful. You can now log in with your new password.', 'success')
                return redirect(url_for('login_route.login'))
            else:
                flash('User not found. Please try again.', 'error')
        else:
            flash('Passwords do not match. Please try again.', 'error')

    return render_template('reset_password.html')