from flask import Flask
from flask_app.models import db
from flask_app.config import Config

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.postgresdb_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)
    db.init_app(app)
    
    @app.before_request
    def create_tables():
        db.create_all()

    from flask_app.login_route.login_route import login_route
    from flask_app.registration_route.registration_route import registration_route
    from flask_app.recover_password.recover_password import recover_password
    from flask_app.get_location_route.get_location_route import get_location_route
    from flask_app.incident_route.incident_route import incident_route
    
    app.register_blueprint(login_route)
    app.register_blueprint(registration_route)
    app.register_blueprint(recover_password)
    app.register_blueprint(get_location_route)
    app.register_blueprint(incident_route)
    return app