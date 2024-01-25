from flask_app.models import db, User
from flask_app.common_functiom import hash_password
from flask import render_template, url_for, request, flash, redirect, Blueprint, abort

registration_route = Blueprint('registration_route', __name__)

# Your existing routes
@registration_route.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hash_password(request.form['password'])
        phone = request.form['phone']
        address = request.form['address']
        pincode = request.form['pincode']
        city = request.form['city']
        country = request.form['country']

        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return render_template('user_registration.html', error='Username or email already exists')

        # Creating a new user
        new_user = User(username=username, email=email, password=password, phone=phone, address=address, pincode=pincode, city=city, country=country)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        flash('Registration succesful. Please Login')
        return redirect(url_for('login_route.login'))

    return render_template('user_registration.html')