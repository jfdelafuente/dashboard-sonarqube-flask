SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

-- create a database
CREATE DATABASE IF NOT EXISTS infocodes;

-- use that db
USE infocodes;

DROP TABLE IF EXISTS metricas;

CREATE TABLE metricas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    aplicacion TEXT,
    fecha TEXT,
    bugs INTEGER,
    reliability_rating INTEGER,
    reliability_label TEXT,
    vulnerabilities INTEGER,
    security_rating INTEGER,
    security_label TEXT,
    code_smells INTEGER,
    sqale_rating INTEGER,
    sqale_label TEXT,
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
    reliability_label TEXT,
    vulnerabilities INTEGER,
    security_rating INTEGER,
    security_label TEXT,
    code_smells INTEGER,
    sqale_rating INTEGER,
    sqale_label TEXT,
    alert_status TEXT,
    app_sonar TEXT
);

DROP TABLE IF EXISTS proveedor;

CREATE TABLE proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aplicacion TEXT,
    proveedor TEXT
);