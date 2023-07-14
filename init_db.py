import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def extract_from_csv(file_to_process) -> pd.DataFrame: 
    dataframe = pd.read_csv(file_to_process, sep=';') 
    return dataframe


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def create_schema(conn):
    with open('schema.sql') as f:
        conn.executescript(f.read())
        
    
def create_metricas(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    sql =''' INSERT INTO metricas (name, aplicacion, fecha, bugs, reliability_rating, reliability_label, vulnerabilities, security_rating, security_label, code_smells, sqale_rating, sqale_label, alert_status, app_sonar) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
                
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_historico(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    
    sql =''' INSERT INTO historico (name, aplicacion, fecha, bugs, reliability_rating, reliability_label, vulnerabilities, security_rating, security_label, code_smells, sqale_rating, sqale_label, alert_status, app_sonar) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
                
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_proveedores(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    
    sql =''' INSERT INTO proveedor (aplicacion, proveedor) 
                VALUES(?, ?) '''
                
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def main():
    
    database = r"" + os.environ['DATABASE']
    # datos_csv = r"" + os.environ['DATOS_LABELS_CSV']
    # historico_csv = r"" + os.environ['HISTORICO_CSV']
    datos_csv = 'metricas.csv'
    historico_csv = 'historico.csv'
    proveedor_csv = "proveedores.csv"
    
    print("Datos metricas : %s \nDatos Historicos : %s \nDatos Proveedor : %s" % (datos_csv, historico_csv, proveedor_csv))
    
    # create a database connection
    conn = create_connection(database)
    print("Creando schema ...")
    create_schema(conn)

    print("Extract datos metricas csv ...")
    df_measures = extract_from_csv(datos_csv)
    with conn:
        for i, measure in df_measures.iterrows():
            project = (measure["proyecto"] +"-application-java", 
                       measure["aplicacion"],
                       measure["date"], 
                       int(measure["bugs"]),
                       int(measure["reliability_rating"]),
                       measure["reliability_label"],
                       int(measure["vulnerabilities"]),
                       int(measure["security_rating"]),
                       measure["security_label"],
                       int(measure["code_smells"]),
                       int(measure["sqale_rating"]),
                       measure["sqale_label"],
                       measure["alert_status"],
                       measure["app_sonar"]
                       )

            project_id = create_metricas(conn, project)
        print(project_id)


    print("Extract datos historico csv ...")
    df_measures = extract_from_csv(historico_csv)
    with conn:    
        for i, measure in df_measures.iterrows():
            project = (measure["proyecto"] +"-application-java", 
                       measure["aplicacion"],
                       measure["date"], 
                       int(measure["bugs"]),
                       int(measure["reliability_rating"]),
                       measure["reliability_label"],
                       int(measure["vulnerabilities"]),
                       int(measure["security_rating"]),
                       measure["security_label"],
                       int(measure["code_smells"]),
                       int(measure["sqale_rating"]),
                       measure["sqale_label"],
                       measure["alert_status"],
                       measure["app_sonar"]
                       )
            
            project_id = create_historico(conn, project)
        print(project_id)
        
    print("Extract datos proveedor csv ...")
    df_measures = extract_from_csv(proveedor_csv)
    with conn:    
        for i, measure in df_measures.iterrows():
            project = (measure["aplicacion"],
                       measure["proveedor"]
                       )
            
            project_id = create_proveedores(conn, project)
        print(project_id)
        
    conn.close()


if __name__ == '__main__':
    main()