from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

# class Base(DeclarativeBase):
#   pass
# db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
migrate = Migrate()
bootstrap = Bootstrap()
csrf = CSRFProtect()

login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"