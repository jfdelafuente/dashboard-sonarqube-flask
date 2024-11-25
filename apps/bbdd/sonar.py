import sqlite3
# import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    DATABASE_URL = r"" + os.environ['DATABASE']
    conn = sqlite3.connect(DATABASE_URL)
    # DATABASE_URL = "postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]"
    # conn = psycopg2.connect(DATABASE_URL)
    
    conn.row_factory = sqlite3.Row
    return conn      
 
def getAllMetricas():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute('SELECT * FROM metricas').fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getDistinctHistorico():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute('SELECT DISTINCT aplicacion FROM historico').fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getOneHistorico(project):
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT * FROM historico where aplicacion=?", (project,)).fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getAllHistorico(project):
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT name, aplicacion, fecha, bugs, vulnerabilities, code_smells FROM historico where aplicacion=?", (project,)).fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getRepositorios():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT aplicacion, COUNT(*) AS NUM_REPO \
                          from metricas GROUP BY aplicacion \
                          HAVING COUNT(*) > 2 \
                          ORDER BY COUNT(*) DESC;").fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getDistinctProveedor():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute('SELECT DISTINCT proveedor FROM proveedor INNER JOIN metricas on metricas.aplicacion=proveedor.aplicacion').fetchall()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def getOneProveedor(project):
    print("Realizando consulta")
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT * FROM metricas \
                                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                                WHERE proveedor.proveedor=?", (project,)).fetchall()
        print(scores)
        conn.close()
    except Exception as e:
        print(e)
        conn.close()
    return scores

def get_E_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and (metricas.reliability_rating='5' or metricas.reliability_rating='4') GROUP BY metricas.aplicacion".format(proveedor)
        # print(f"Realizando consulta : {query}")        
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores

def get_C_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and metricas.reliability_rating='3' GROUP BY metricas.aplicacion".format(proveedor)
        # print(f"Realizando consulta : {query}")        
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores

def get_A_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and (metricas.reliability_rating='1' or metricas.reliability_rating='2') GROUP BY metricas.aplicacion".format(proveedor)
        # print(f"Realizando consulta : {query}")        
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores