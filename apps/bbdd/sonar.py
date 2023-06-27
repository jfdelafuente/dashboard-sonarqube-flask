import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    database = r"" + os.environ['DATABASE']
    conn = sqlite3.connect(database)
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