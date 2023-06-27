DROP TABLE IF EXISTS metricas;

CREATE TABLE metricas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    aplicacion TEXT,
    fecha TEXT,
    bugs INTEGER,
    reliability_rating INTEGER,
    vulnerabilities INTEGER,
    security_rating INTEGER,
    code_smells INTEGER,
    sqale_rating INTEGER,
    alert_status TEXT,
    app_sonar TEXT
);

DROP TABLE IF EXISTS historico;

CREATE TABLE historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    aplicacion TEXT,
    fecha TEXT,
    bugs INTEGER,
    reliability_rating INTEGER,
    vulnerabilities INTEGER,
    security_rating INTEGER,
    code_smells INTEGER,
    sqale_rating INTEGER,
    alert_status TEXT,
    app_sonar TEXT
);