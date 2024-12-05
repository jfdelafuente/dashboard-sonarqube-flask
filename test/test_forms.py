from infocodest.accounts.forms import RegisterForm, LoginForm



def test_validate_success_register_form(test_client):
        # Ensure correct data validates.
        form = RegisterForm(username= "new", email="new@test.com", password="example", confirm="example")
        assert form.validate() == "True"

# def test_validate_invalid_password_format(test_client):
#         # Ensure incorrect data does not validate.
#         form = RegisterForm(email="new@test.com", password="example", confirm="")
#         assert form.validate() == "False"


# def test_validate_email_already_registered(test_client):
#         # Ensure user can't register when a duplicate email is used
#         form = RegisterForm(
#             email="ad@min.com", password="admin_user", confirm="admin_user"
#         )
#         self.assertFalse(form.validate())
        
# def test_validate_success_login_form(test_client):
#         # Ensure correct data validates.
#         form = LoginForm(email="ad@min.com", password="admin_user")
#         self.assertTrue(form.validate())

# def test_validate_invalid_email_format(test_client):
#         # Ensure invalid email format throws error.
#         form = LoginForm(email="unknown", password="example")
#         self.assertFalse(form.validate())