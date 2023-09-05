# Cómo construir una aplicación web completa con Python y SQLite3

Ejecutamos por este orden:

python3.8 -m venv venv

👉 Set Up for Unix

$ virtualenv venv
$ source venv/bin/activate

# Para desactivar
$ deactivate

# upgrade pip
$ python -m pip install --upgrade pip

$ pip3 install -r requirements.txt

Set Up Flask Environment

$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ export FLASK_DEBUG=true

👉 Set Up for Windows

Install modules via VENV (windows)

$ virtualenv venv
$ .\venv\Scripts\activate
$ pip3 install -r requirements.txt

Set Up Flask Environment

$ # CMD
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "Development"
$ $env:FLASK_DEBUG = "true"

Start the app

$ flask run

$ flask --app run --debug run

At this point, the app runs at http://127.0.0.1:5000/.

## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://github.com/appseed-projects/<YOUR_BUILD_ID>.git
$ cd <YOUR_BUILD_ID>
```

<br />

> **Step 2** - Edit `.env` and set `DEBUG=True`. This will activate the `SQLite` persistance. 

```txt
DEBUG=True
```

<br />

> **Step 3** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />



(venv) python -m pytest --setup-show --cov=apps --cov-report=html




ultimas modificaciones

lanzar test_measures.ipynb para extraer los datos del proyecto de sonar.
Esos datos se transforman y se creand dos nuevos ficheros; historico.csv y metricas.csv

Posteriormente se lanza init_db.py para recrear la bbdd y cargar los csv (historico, metrica y proveedores)