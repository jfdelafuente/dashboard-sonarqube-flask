from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from infocodest.models.users import User


# def populate_db():
#     """
#     Adds fake data to the database.
#     """
#     admin = User(password="shh", username="chris")
#     db.session.add(admin)
#     db.session.commit()
