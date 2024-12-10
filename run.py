import os
from sys import exit
# from flask_migrate import Migrate
from flask_minify import Minify
from infocodest import create_app
# from infocodest.extensions import db
from config import config_dict
from dotenv import load_dotenv


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# WARNING: Don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

# The configuration
get_config_mode = "Debug" if DEBUG else "Production"

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit("Error: Invalid <config_mode>. Expected values [Development, Testing, Production] ")

app = create_app(app_config)
# Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if DEBUG:
    app.logger.info("DEBUG            = " + str(DEBUG))
    app.logger.info("ENTORNO          = " + get_config_mode.capitalize())
    app.logger.info("FLASK_ENV        = " + app_config.FLASK_ENV)
    app.logger.info("Page Compression = " + "FALSE" if DEBUG else "TRUE")
    app.logger.info("DBMS             = " + app_config.SQLALCHEMY_DATABASE_URI)


if __name__ == "__main__":
    app.run()
