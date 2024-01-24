from geopy.geocoders import Nominatim

# Displaying address details
# print("Zipcode:",zipcode)
# print("Details of the Zipcode:")
# print(location)

from flask import render_template, url_for, request, flash, redirect, Blueprint, abort, jsonify
from flask_app.common_functiom import hash_password
from flask_app.models import db, User

get_location_route = Blueprint('get_location_route', __name__)

# Your existing routes
@get_location_route.route('/get_location', methods=['GET'])
def get_location():
    pin_code = request.args.get('pin_code')
    # Using Nominatim Api
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    try:
        location = geolocator.geocode(pin_code)
        if location:
            # Access the address dictionary
            address = str(location)
            split_address = address.split(",")
            
            return jsonify({'statusCode': 1, 'message': {'city': split_address[-3], 'country': split_address[-1]}})
        else:
            return jsonify({'statusCode': 0, 'message': 'Location not found'})
    except Exception as error:
        print(error)
        return jsonify({'statusCode': -1, 'message': 'internal server error'})