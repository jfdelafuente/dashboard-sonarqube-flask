from flask import Blueprint

charts_bp = Blueprint(
    "charts", __name__, template_folder="templates", static_folder="static"
)

from . import views
