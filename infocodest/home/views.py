from flask import render_template, request
from flask_login import login_required
from infocodest.home import home_bp
from infocodest.models.metricas import Metrica

# from infocodest.models.stat import Stat
# from infocodest.models.historico import Historico
from infocodest.models.proveedor import Proveedor

# from infocodest.models.daily import Daily
from datetime import datetime

import infocodest.models.database as consulta
from .consultas import (
    get_metricas,
    get_dailys,
    get_distinct_providers,
    get_metricas_aplicacion,
    get_distinct_apps,
    get_historico_name,
    get_stats,
    get_metricas_proveedor,
    get_stats_aplicacion,
    get_stats_proveedor,
    get_dailys_proveedor,
    get_dailys_details_aplicacion,
    get_dailys_details_repo,
)


# from sqlalchemy.sql import func
# from sqlalchemy import and_

# home_bp = Blueprint("home", __name__)


@home_bp.route("/")
@login_required
def home():
    return render_template(
        "home/index.html", date=datetime.now(), dato=consulta.getDatosMetricas()
    )


@home_bp.route("/metricas")
@login_required
def metricas():
    # metricas = Metrica.query.all()
    return render_template(
        "home/metricas/metricas.html",
        scores=get_metricas(),
        dato=consulta.getDatosMetricas(),
    )


@home_bp.route("/metricas/aplicacion", methods=("GET", "POST"))
@login_required
def historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        # print(f'Proyect name {project}')
        return render_template(
            "home/metricas/historico.html",
            apps=apps,
            scores=get_metricas_aplicacion(project),
            project=project,
            dato=consulta.getDatosAplicacion(project),
            success=True,
        )
    else:
        return render_template("home/metricas/historico.html", apps=apps)


@home_bp.route("/metricas/proveedores", methods=("GET", "POST"))
@login_required
def proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/metricas/proveedores.html",
            apps=apps,
            scores=get_metricas_proveedor(project),
            proveedor=project,
            dato=consulta.getDatosProveedor(project),
            success=True,
        )
    else:
        return render_template("home/metricas/proveedores.html", apps=apps)


@home_bp.route("/kpis")
@login_required
def kpis():
    kpis = Metrica.query.all()
    return render_template(
        "home/kpis/kpis.html", scores=kpis, dato=consulta.getDatosMetricas()
    )


@home_bp.route("/kpis/proveedores", methods=("GET", "POST"))
@login_required
def kpis_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_proveedores.html",
            apps=apps,
            scores=Metrica.query.join(
                Proveedor, Metrica.aplicacion == Proveedor.aplicacion
            )
            .filter(Proveedor.proveedor == project)
            .order_by(Metrica.aplicacion.desc()),
            proveedor=project,
            dato=consulta.getDatosProveedor(project),
            success=True,
        )
    else:
        return render_template("home/kpis/kpis_proveedores.html", apps=apps)


@home_bp.route("/kpis/aplicacion", methods=("GET", "POST"))
@login_required
def kpis_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_historico.html",
            apps=apps,
            scores=get_metricas_aplicacion(project),
            date=datetime.now(),
            proveedor=project,
            dato=consulta.getDatosAplicacion(project),
            success=True,
        )
    else:
        return render_template("home/kpis/kpis_historico.html", apps=apps)


@home_bp.route("/stats")
@login_required
def stats():
    return render_template(
        "home/stats/stats.html", scores=get_stats(), dato=consulta.getDatosMetricas()
    )


@home_bp.route("/stats/proveedores", methods=("GET", "POST"))
@login_required
def stats_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_proveedores.html",
            apps=apps,
            scores=get_stats_proveedor(project),
            proveedor=project,
            dato=consulta.getDatosProveedor(project),
            success=True,
        )
    else:
        return render_template("home/stats/stats_proveedores.html", apps=apps)


@home_bp.route("/metricas/aplicacion/<project>", methods=["GET", "POST"])
def show_historico_project(project):
    apps = get_distinct_apps()
    return render_template(
        "home/metricas/historico.html",
        apps=apps,
        scores=get_metricas_aplicacion(project),
        project=project,
        dato=consulta.getDatosAplicacion(project),
        success=True,
    )


@home_bp.route("/metricas/aplicacion/<project>/<name>", methods=["GET", "POST"])
def show_historico_name(project, name):
    # apps = get_distinct_apps()
    return render_template(
        "home/metricas/charts_historico.html",
        # apps=apps,
        scores=get_historico_name(project, name),
        project=project,
        date=datetime.now(),
        name=name,
        success=True,
    )


@home_bp.route("/kpis/aplicacion/<project>")
def show_kpis_historico_project(project):
    apps = get_distinct_apps()
    return render_template(
        "home/kpis/kpis_historico.html",
        apps=apps,
        scores=get_metricas_aplicacion(project),
        project=project,
        date=datetime.now(),
        dato=consulta.getDatosAplicacion(project),
        success=True,
    )


@home_bp.route("/kpis/aplicacion/<project>/<name>")
def show_kpis_historico_name(project, name):
    apps = get_distinct_apps()
    return render_template(
        "home/kpis/kpis_charts_historico.html",
        apps=apps,
        scores=get_historico_name(project, name),
        name=name,
        date=datetime.now(),
        project=project,
        # dato=consulta.getDatosName(name),
        success=True,
    )


@home_bp.route("/stats/aplicacion", methods=("GET", "POST"))
@login_required
def stats_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_historico.html",
            apps=apps,
            scores=get_stats_aplicacion(project),
            proveedor=project,
            dato=consulta.getDatosAplicacion(project),
            success=True,
        )
    else:
        return render_template("home/stats/stats_historico.html", apps=apps)


# peticion a moodificar para extraer las stats de cada repo del <project>
@home_bp.route("/stats/aplicacion/<project>", methods=("GET", "POST"))
def show_stats_historico_project(project):
    apps = get_distinct_apps()
    return render_template(
        "home/stats/stats_historico.html",
        apps=apps,
        scores=get_stats_aplicacion(project),
        proveedor=project,
        dato=consulta.getDatosAplicacion(project),
        success=True,
    )


@home_bp.route("/dailys")
def dailys():
    return render_template(
        "home/dailys/dailys.html", scores=get_dailys(), dato=consulta.getDatosMetricas()
    )


@home_bp.route("/dailys/proveedores", methods=("GET", "POST"))
def dailys_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        print(project)
        return render_template(
            "home/dailys/dailys_proveedores_chart.html",
            apps=apps,
            date=datetime.now(),
            scores=get_dailys_proveedor(project),
            project=project,
            dato=consulta.getDatosProveedor(project),
            success=True,
        )
    else:
        return render_template("home/dailys/dailys_proveedores.html", apps=apps)


@home_bp.route("/dailys/aplicacion", methods=("GET", "POST"))
def dailys_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/dailys/dailys_historico_chart.html",
            apps=apps,
            scores=get_dailys_details_aplicacion(project),
            project=project,
            date=datetime.now(),
            dato=consulta.getDatosAplicacion(project),
            success=True,
        )
    else:
        return render_template("home/dailys/dailys_historico.html", apps=apps)


@home_bp.route("/dailys/aplicacion/<project>", methods=["GET", "POST"])
def show_dailys_project(project):
    apps = get_distinct_apps()
    return render_template(
        "home/dailys/dailys_historico_chart.html",
        apps=apps,
        date=datetime.now(),
        scores=get_dailys_details_aplicacion(project),
        project=project,
        dato=consulta.getDatosAplicacion(project),
        success=True,
    )


@home_bp.route("/dailys/aplicacion/<project>/<repo>", methods=["GET", "POST"])
def show_dailys_repo(project, repo):
    apps = get_distinct_apps()
    return render_template(
        "home/dailys/dailys_historico_repo_chart.html",
        apps=apps,
        date=datetime.now(),
        scores=get_dailys_details_repo(project, repo),
        project=project,
        repo=repo,
        dato=consulta.getDatosRepositorios(project, repo),
        success=True,
    )
