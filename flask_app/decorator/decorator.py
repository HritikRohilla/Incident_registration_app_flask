import time
from functools import wraps
from flask import flash, url_for, session, redirect


def login_required(f):
    @wraps(f)
    def deco_function(*args, **kwargs):
        # Check if the user is logged in
        if 'user_id' in session:
            return f(*args, **kwargs)
        flash("Please Login First")
        return redirect(url_for('login_route.login'))
    return deco_function

def already_loggedin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in session:
            return redirect(url_for('incident_route.home'))
        else:
            return f(*args, **kwargs)
    return wrap