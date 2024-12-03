
from infocodest.models.metricas import Metrica
from infocodest.models.stat import Stat
from infocodest.models.historico import Historico
from infocodest.models.proveedor import Proveedor
from infocodest.models.daily import Daily

from sqlalchemy.sql import func
from sqlalchemy import and_


def get_distinct_apps():
    return Metrica.query.with_entities(Metrica.aplicacion).distinct().all()

def get_distinct_providers():
    return Proveedor.query.join(Metrica, Proveedor.aplicacion == Metrica.aplicacion).with_entities(Proveedor.proveedor).distinct().all()

def get_metricas():
    metricas = Metrica.query \
        .join(Proveedor, Proveedor.aplicacion == Metrica.aplicacion) \
        .order_by(Metrica.fecha.desc()) \
        .with_entities( Metrica.aplicacion,
                        Metrica.repo,
                        Metrica.size,
                        Metrica.fecha,
                        Metrica.reliability_label,
                        Metrica.reliability_rating,
                        Metrica.bugs,
                        Metrica.security_label,
                        Metrica.security_rating,
                        Metrica.vulnerabilities,
                        Metrica.sqale_label,
                        Metrica.sqale_rating,
                        Metrica.code_smells,
                        Metrica.alert_status,
                        Metrica.quality_gate,
                        Metrica.project,
                        Metrica.coverage,
                        Metrica.unit_tests,
                        Proveedor.tipo
                    ) \
        .all()
    return metricas


def get_stats():
    stats = Stat.query \
        .join(Proveedor, Proveedor.aplicacion == Stat.aplicacion) \
        .with_entities( Stat.aplicacion,
                        Stat.repos,
                        Stat.reliability_label,
                        Stat.reliability_rating,
                        Stat.security_label,
                        Stat.security_rating,
                        Stat.sqale_label,
                        Stat.sqale_rating,
                        Stat.alert_status_label,
                        Stat.alert_status_ok,
                        Stat.dloc_label,
                        Stat.dloc_rating,
                        Stat.coverage_label,
                        Stat.coverage_rating,
                        Proveedor.tipo
                    ) \
        .all()
    return stats


def get_metricas_aplicacion(project):
    return Metrica.query \
        .join(Proveedor, Metrica.aplicacion == Proveedor.aplicacion) \
        .filter(Metrica.aplicacion == project) \
        .order_by(Metrica.fecha.desc()) \
        .with_entities( Metrica.aplicacion,
                        Metrica.repo,
                        Metrica.size,
                        Metrica.fecha,
                        Metrica.reliability_label,
                        Metrica.reliability_rating,
                        Metrica.bugs,
                        Metrica.security_label,
                        Metrica.security_rating,
                        Metrica.vulnerabilities,
                        Metrica.sqale_label,
                        Metrica.sqale_rating,
                        Metrica.code_smells,
                        Metrica.alert_status,
                        Metrica.quality_gate,
                        Metrica.project,
                        Metrica.coverage,
                        Metrica.unit_tests,
                        Proveedor.tipo
                    ) \
        .all()


def get_stats_aplicacion(project):
    return Stat.query \
        .join(Proveedor, Stat.aplicacion == Proveedor.aplicacion) \
        .filter(Stat.aplicacion == project) \
        .with_entities( Stat.aplicacion,
                        Stat.repos,
                        Stat.reliability_label,
                        Stat.reliability_rating,
                        Stat.security_label,
                        Stat.security_rating,
                        Stat.sqale_label,
                        Stat.sqale_rating,
                        Stat.alert_status_label,
                        Stat.alert_status_ok,
                        Stat.dloc_label,
                        Stat.dloc_rating,
                        Stat.coverage_label,
                        Stat.coverage_rating,
                        Proveedor.tipo
                    ) \
        .all()


def get_metricas_proveedor(project):
    return Metrica.query \
        .join(Proveedor, Metrica.aplicacion == Proveedor.aplicacion) \
        .filter(Proveedor.proveedor == project) \
        .order_by(Metrica.aplicacion.asc(), Metrica.fecha.desc()) \
        .with_entities( Metrica.aplicacion,
                        Metrica.repo,
                        Metrica.size,
                        Metrica.fecha,
                        Metrica.reliability_label,
                        Metrica.reliability_rating,
                        Metrica.bugs,
                        Metrica.security_label,
                        Metrica.security_rating,
                        Metrica.vulnerabilities,
                        Metrica.sqale_label,
                        Metrica.sqale_rating,
                        Metrica.code_smells,
                        Metrica.alert_status,
                        Metrica.quality_gate,
                        Metrica.project,
                        Metrica.coverage,
                        Metrica.unit_tests,
                        Proveedor.tipo
                    )


def get_stats_proveedor(project):
    return Stat.query \
        .join(Proveedor, Stat.aplicacion == Proveedor.aplicacion) \
        .filter(Proveedor.proveedor == project) \
        .with_entities( Stat.aplicacion,
                        Stat.repos,
                        # Stat.size,
                        # Stat.fecha,
                        Stat.reliability_label,
                        Stat.reliability_rating,
                        Stat.security_label,
                        Stat.security_rating,
                        Stat.sqale_label,
                        Stat.sqale_rating,
                        Stat.alert_status_label,
                        Stat.alert_status_ok,
                        Stat.dloc_label,
                        Stat.dloc_rating,
                        Stat.coverage_label,
                        Stat.coverage_rating,
                        Proveedor.tipo
                    ) \
        .all()


def get_dailys():
    return Daily.query.filter(Daily.created_on == date.today()-timedelta(days=1)).group_by(Daily.aplicacion) \
        .with_entities( Daily.aplicacion,
                        func.count('*').label('repo'),
                        Daily.proveedor,
                        Daily.created_on,
                        func.sum(Daily.num_bugs).label('num_bugs'),
                        func.sum(Daily.num_vulnerabilities).label('num_vulnerabilities'),
                        func.sum(Daily.num_code_smells).label('num_code_smells'),
                        func.sum(Daily.num_quality).label('num_quality'),
                        func.sum(Daily.num_analisis).label('num_analisis')
                    ) \
        .all()


def get_dailys_proveedor(proveedor):
    return Daily.query.filter(Daily.created_on == date.today()-timedelta(days=1)).group_by(Daily.aplicacion) \
        .filter(Daily.proveedor == proveedor) \
        .with_entities( Daily.aplicacion,
                        func.count('*').label('repo'),
                        Daily.proveedor,
                        Daily.created_on,
                        func.sum(Daily.num_bugs).label('num_bugs'),
                        func.sum(Daily.num_vulnerabilities).label('num_vulnerabilities'),
                        func.sum(Daily.num_code_smells).label('num_code_smells'),
                        func.sum(Daily.num_quality).label('num_quality'),
                        func.sum(Daily.num_analisis).label('num_analisis')
                    ) \
        .all()


def get_dailys_details_aplicacion(project):
    return Daily.query.filter(Daily.created_on == date.today()-timedelta(days=1)) \
        .filter(Daily.aplicacion == project) \
        .with_entities( Daily.aplicacion,
                        Daily.repo,
                        Daily.proveedor,
                        Daily.created_on,
                        Daily.num_bugs,
                        Daily.num_vulnerabilities,
                        Daily.num_code_smells,
                        Daily.num_quality,
                        Daily.num_analisis
                    ) \
        .all()


def get_dailys_details_repo(aplicacion, repo):
    return Daily.query.filter(Daily.created_on == date.today()-timedelta(days=1)) \
        .filter(and_(Daily.repo==repo, Daily.aplicacion==aplicacion)) \
        .with_entities( Daily.aplicacion,
                        Daily.repo,
                        Daily.proveedor,
                        Daily.created_on,
                        Daily.num_bugs,
                        Daily.num_vulnerabilities,
                        Daily.num_code_smells,
                        Daily.num_quality,
                        Daily.num_analisis
                    ) \
        .all()


def get_historico_name(project, name):
    return Historico.query \
        .join(Proveedor, Historico.aplicacion == Proveedor.aplicacion) \
        .filter(and_(Historico.repo == name, Historico.aplicacion== project)) \
        .order_by(Historico.fecha.desc()) \
        .with_entities( Historico.aplicacion,
                        Historico.repo,
                        Historico.size,
                        Historico.fecha,
                        Historico.reliability_label,
                        Historico.reliability_rating,
                        Historico.bugs,
                        Historico.security_label,
                        Historico.security_rating,
                        Historico.vulnerabilities,
                        Historico.sqale_label,
                        Historico.sqale_rating,
                        Historico.code_smells,
                        Historico.alert_status,
                        Historico.quality_gate,
                        Historico.project,
                        Historico.coverage,
                        Historico.unit_tests,
                        Proveedor.tipo
                    ) \
        .all()
