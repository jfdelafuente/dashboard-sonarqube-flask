from flask import render_template, jsonify, url_for, redirect, request
from apps.api import api
from datetime import datetime
from apps.bbdd.sonar import getAllMetricas, getDistinctHistorico, getOneHistorico, getAllHistorico, getRepositorios


@api.route("/historico/<project>")
def historico_project(project):
    data = {}
    scores = getAllHistorico(project)
    data["project_name"] = [row[0] for row in scores]
    data["aplicacion"] = [row[1] for row in scores]
    data["data"] = [row[2] for row in scores]
    data["bugs"] = [row[3] for row in scores]
    data["vulnerabilities"] = [row[4] for row in scores]
    data["codesmells"] = [row[5] for row in scores]
    return jsonify(data)

@api.route("/historico/<project>/<name>")
def historico_name(project, name):
    data = {}
    scores = getAllHistorico(project)
    data["project_name"] = [row[0] for row in scores]
    data["aplicacion"] = [row[1] for row in scores]
    data["data"] = [row[2] for row in scores]
    data["bugs"] = [row[3] for row in scores]
    data["vulnerabilities"] = [row[4] for row in scores]
    data["codesmells"] = [row[5] for row in scores]
    return jsonify(data)


@api.route("/show/historico/<project>/<name>")
def show_historico_name(project, name):
    return redirect(url_for('home.charts_test'))


@api.route("/charts_data")
def charts_data():
    data = {}
    scores = getRepositorios()
    labels = [row[0] for row in scores]
    values = [row[1] for row in scores]
    data["labels"] = labels
    data["values"] = values
    return jsonify(data)
