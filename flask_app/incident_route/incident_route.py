import random, json
from datetime import datetime
from flask_app.models import db, Incident
from flask_app.decorator.decorator import login_required
from flask import render_template, request, flash, Blueprint, session, redirect, url_for, jsonify

incident_route = Blueprint('incident_route', __name__)

@incident_route.route('/incident', methods=['GET', 'POST'])
@login_required
def incident():
    if request.method == 'POST':
        incident_type = request.form.get('incidentType')
        reporter_name = request.form.get('reporterName')
        incident_details = request.form.get('incidentDetails')
        priority = request.form.get('priority')
        incident_status = request.form.get('incidentStatus')
        phone = request.form.get('phone')
        address = request.form.get('address')
        pincode = request.form.get('pincode')
        city = request.form.get('city')
        country = request.form.get('country')

        # Auto-generate Incident ID
        incident_id = f'RMG{random.randint(10000, 99999)}{datetime.now().year}'

        # Checking uniqueness of Incident ID
        while Incident.query.filter_by(id=incident_id).first():
            incident_id = f'RMG{random.randint(10000, 99999)}{datetime.now().year}'

        # getting user_id from session
        user_id = session['user_id']

        # Creating and add the new incident to the database
        new_incident = Incident(
            id=incident_id,
            incident_type=incident_type,
            reporter_name=reporter_name,
            incident_details=incident_details,
            priority=priority,
            incident_status=incident_status,
            user_id=user_id,
            phone=phone, 
            address=address, 
            pincode=pincode, 
            city=city, 
            country=country
        )

        db.session.add(new_incident)
        db.session.commit()

        flash("Incident created successfully")
        return redirect(url_for('incident_route.home'))
    return render_template('incident.html')

@incident_route.route('/home')
@login_required
def home():
    # Get the user ID from the session
    user_id = session['user_id']

    user_incidents = Incident.query.filter_by(user_id=user_id).all()

    return render_template('home.html', incidents=user_incidents)


@incident_route.route('/edit_incident/<incident_id>', methods=['GET', 'POST'])
@login_required
def edit_incident(incident_id):
    # Fetch the incident from the database
    incident = Incident.query.get_or_404(incident_id)

    # If incident is closed, redirect to the incident details page
    if incident.incident_status == 'Closed':
        return redirect(url_for('incident_route.home'))

    if request.method == 'POST':
        incident.priority = request.form['priority']
        incident.incident_status = request.form['incidentStatus']
        incident.incident_details = request.form['incidentDetails']

        db.session.commit()

        # Redirect to the incident details page (or handle accordingly)
        return redirect(url_for('incident_route.home'))

    return render_template('edit_incident.html', incident=incident)


# TODO for now this route is open but user can search from UI also
@incident_route.route('/search_incident/<incident_id>', methods=['GET'])
# @login_required
def search_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)

    # converting data into dict
    incident_data = incident.__dict__

    # Removing attributes that has ' _ ' in string
    incident_data = {key: value for key, value in incident_data.items() if not key.startswith('_')}

    return jsonify(incident_data), 200
