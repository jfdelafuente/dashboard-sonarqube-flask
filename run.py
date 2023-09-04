import os
from   flask_minify  import Minify
from   sys import exit

from config import config_dict
from apps import create_app

# The configuration
get_config_mode = os.getenv('FLASK_ENV', 'Development')

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Development, Production] ')

app = create_app(app_config)

if not app_config.DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if app_config.DEBUG:
    app.logger.info('DEBUG            = ' + str(app_config.DEBUG)             )
    app.logger.info('FLASK_ENV        = ' + app_config.FLASK_ENV   )
    app.logger.info('Page Compression = ' + 'FALSE' if app_config.DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT )

if __name__ == "__main__":
    app.run()