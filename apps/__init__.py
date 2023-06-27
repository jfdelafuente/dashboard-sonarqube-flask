from flask_bootstrap import Bootstrap
from flask import Flask
from .errorhandlers import error_404, error_500, error_401
from flask_cors import CORS


### Helper Functions ###
def configure_database(app):
    
    @app.before_first_request
    def initialize_database():
        pass
    
    @app.teardown_request
    def shutdown_session(exception=None):
        pass


def register_blueprints(app):
    from apps.home import home
    from apps.api import api
    from apps.auth import auth

    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(auth, url_prefix='/auth')
    
def initialize_extensions(app):
    CORS(app, resources={r"/*": {"origins": "*"}})
    Bootstrap(app)


def register_error_handlers(app):
    app.register_error_handler(401, error_401)
    app.register_error_handler(404, error_404)
    app.register_error_handler(500, error_500)

    
def configure_logging(app):
  pass


### Application Factory ###
def create_app(config):
    
    app = Flask(__name__)
    # Configure the flask app instance
    app.config.from_object(config)
    # Register blueprints
    register_blueprints(app)
    # Initialize flask extension objects
    initialize_extensions(app)
    # Configure logging
    configure_logging(app)
    # Register error handlers
    register_error_handlers(app)
    # configure_database(app)
    return app