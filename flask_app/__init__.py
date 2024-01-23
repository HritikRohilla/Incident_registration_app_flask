from flask import Flask
# from flask_app.config import Config

def create_app():
    app = Flask(__name__)
    # app.secret_key = Config.secret_key
    # app.config.from_object(Config)

    from flask_app.login_route.login_route import login_route
    from flask_app.registration_route.registration_route import registration_route
    from flask_app.recover_password.recover_password import recover_password
    
    app.register_blueprint(login_route)
    app.register_blueprint(registration_route)
    app.register_blueprint(recover_password)
    return app