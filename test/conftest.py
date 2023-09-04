import pytest
import os
from apps import create_app
from config import config_dict

@pytest.fixture()
def app():
    get_config_mode = 'Testing'
    app_config = config_dict[get_config_mode.capitalize()]
    app = create_app(app_config)
    # other setup can go here
    yield app
    # clean up / reset resources here
    

@pytest.fixture()
def test_client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
