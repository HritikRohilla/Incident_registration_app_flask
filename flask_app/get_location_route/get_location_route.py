from geopy.geocoders import Nominatim
from flask import request, Blueprint, jsonify
from flask_app.decorator.decorator import login_required

get_location_route = Blueprint('get_location_route', __name__)


@get_location_route.route('/get_location', methods=['GET'])
def get_location():
    pin_code = request.args.get('pin_code')
    # Using Nominatim Api
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    try:
        location = geolocator.geocode(pin_code)
        if location:
            address = str(location)
            split_address = address.split(",")
            
            return jsonify({'statusCode': 1, 'message': {'city': split_address[-3], 'country': split_address[-1]}})
        else:
            return jsonify({'statusCode': 0, 'message': 'Location not found'})
    except Exception as error:
        print(error)
        return jsonify({'statusCode': -1, 'message': 'internal server error'})