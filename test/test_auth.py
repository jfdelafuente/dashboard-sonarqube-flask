import json


def test_home_auth(test_client):
    response = test_client.get("/auth")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/auth/login"


def test_login_page(test_client):
    response = test_client.get("/auth/login")
    assert response.status_code == 200
    assert b"Sonar CFM - Login | Orange" in response.data
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_register_page(test_client):
    response = test_client.get("/auth/register")
    assert response.status_code == 200
    assert b"Sonar CFM - Register | Orange" in response.data


def test_password_page(test_client):
    response = test_client.get("/auth/password")
    assert response.status_code == 200
    assert b"Sonar CFM - Password Reset | Orange" in response.data


def test_logout_redirect(test_client):
    response = test_client.get("/logout")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/index"
