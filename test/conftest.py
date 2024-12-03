import os
import pytest

from infocodest import create_app
from infocodest.database import db
from config import config_dict
from infocodest.models.users import User


@pytest.fixture(scope="module")
def new_user():
    user = User("lolo", "lolo@gmail.com", "lolololo")
    return user


@pytest.fixture(scope='module')
def app():
    get_config_mode = "Testing"
    app_config = config_dict[get_config_mode.capitalize()]
    app = create_app(app_config)
    print(f"DBMS             = {app_config.SQLALCHEMY_DATABASE_URI} ")
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture(scope='module')
def test_client(app):
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!



@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()


    # Insert user data
    default_user = User(
        username="admin_user", email="admin@gmail.com", password="admin_user"
    )
    db.session.add(default_user)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    # db.drop_all()


# @pytest.fixture(scope="function")
# def log_in_default_user(test_client):
#     test_client.post(
#         "/login",
#         data={"username": "lolo", "email": "lolo@gmail.com", "password": "lolololo"},
#     )

#     yield  # this is where the testing happens!

#     test_client.get("/logout")


# @pytest.fixture(scope="function")
# def log_in_default_user(test_client):
#     test_client.post(
#         "login",
#         data={"username": "lolo", "email": "lolo@gmail.com", "password": "lolololo"},
#     )

#     yield  # this is where the testing happens!

#     # Log out the user
#     test_client.get("/logout")
