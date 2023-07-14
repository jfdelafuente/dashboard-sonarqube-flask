from flask import render_template, request, abort
from apps.home import home
from datetime import datetime
from apps.bbdd.sonar import getAllMetricas, getDistinctHistorico, getOneHistorico, getRepositorios, getDistinctProveedor, getOneProveedor


@home.route("/")
@home.route("/index")
def index():
    return render_template('home/index.html', scores=getAllMetricas())

@home.route("/layout-static")
def layout_static():
    return render_template('home/layout-static.html')

@home.route("/metricas")
def metricas():
    return render_template('home/tables.html', scores=getAllMetricas())

@home.route("/charts")
def charts():
    return render_template('home/charts.html')

@home.route("/layout-sidenav-light")
def layout_sidenav_light():
    return render_template('home/layout-sidenav-light.html')

@home.route("/historico",  methods=('GET', 'POST'))
def historico():
    apps = getDistinctHistorico()
    if request.method == 'POST':
        project = request.form['project_name']
        return render_template('home/historico.html', apps=apps, scores=getOneHistorico(project))
    else:
        return render_template('home/historico.html', apps=apps)


@home.route("/charts_test")
def charts_test():
    scores = getRepositorios()
    labels = [row[0] for row in scores]
    values = [row[1] for row in scores]
    return render_template('home/charts_test.html', labels=labels, values=values, date=datetime.now())


@home.route("/charts_historico", methods=('GET', 'POST'))
def charts_historico():
    return render_template('home/charts_historico.html', apps=getDistinctHistorico(), date=datetime.now())

@home.route('/admin')
def admin():
    abort(404)
    
@home.route('/proveedores',  methods=('GET', 'POST'))
def proveedores():
    apps = getDistinctProveedor()
    if request.method == 'POST':
        project = request.form['project_name']
        return render_template('home/proveedores.html', apps=apps, scores=getOneProveedor(project))
    else:
        return render_template('home/proveedores.html', apps=apps)
