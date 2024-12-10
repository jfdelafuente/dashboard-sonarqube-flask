import unittest

from flask.cli import FlaskGroup

# from infocodest import app
from infocodest import create_app
from infocodest.database import db
from infocodest.models.users import User
from config import config_dict

cli = FlaskGroup(create_app(config_dict["Testing"]))


@cli.command("test")
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@cli.command("create_db")
def create_db():
    db.create_all()


@cli.command("drop_db")
def drop_db():
    db.drop_all()


@cli.command("recreate_db")
def recreate_db():
    """Same as running drop_db() and create_db()."""
    drop_db()
    create_db()


@cli.command("create_admin")
def create_admin():
    try:
        email="lolo@gmail.com"
        user = User(email="lolo@gmail.com", password="lolololo", username="lolo")
        db.session.add(user)
        db.session.commit()
        print(f"Admin with email {email} created successfully!")
    except Exception:
        print("Couldn't create admin user.")


if __name__ == "__main__":
    cli()