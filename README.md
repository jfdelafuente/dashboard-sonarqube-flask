# Cómo construir una aplicación web completa con Python y SQLite3

## ✨ Instalar SQLAlchemy

```bash
# cd into SQLAlchemy source distribution
cd path/to/sqlalchemy

# install cython
pip install cython

# optionally build Cython extensions ahead of install
python setup.py build_ext

# run the install
python setup.py install
```

## ✨ Configurar Aplicación

Ejecutamos por este orden:

```bash
python3.8 -m venv venv
```

👉 Set Up for Unix

Instalamos virtualenv
```bash
python3 -m pip install --upgrade pip
pip3 install virtualenv
# Comprobamos la ruta de la version
which virtualenv
which python3
```
```bash
# Creamos entorno virtualizado
virtualenv -p /usr/bin/python3 venv

$ source venv/bin/activate

# Para desactivar
$ deactivate

# upgrade pip
$ python -m pip install --upgrade pip

$ pip3 install -r requirements.txt
```

Set Up Flask Environment

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=true
```

👉 Set Up for Windows

Install modules via VENV (windows)

```bash
virtualenv venv
.\venv\Scripts\activate
pip3 install -r requirements.txt
```

Set Up Flask Environment

```bash
# CMD
set FLASK_APP=run.py
set FLASK_ENV=development

# Powershell
$env:FLASK_APP = ".\run.py"
$env:FLASK_ENV = "Development"
$env:FLASK_DEBUG = "true"
```

Start the app

```bash
$ flask run

o

$ flask --app run --debug run
```

At this point, the app runs at http://127.0.0.1:5000/.

## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
# Get the code
git clone https://github.com/jfdelafuente/dashboard-sonarqube-flask.git
cd dashboard-sonarqube-flask
```

> **Step 2** - Edit `.env` and set `DEBUG=True`. This will activate the `SQLite` persistance.

```txt
DEBUG=True
```

> **Step 3** - Start the APP in `Docker`

```bash
docker build -t flask-image .
docker images
docker run -d -it --name flaskapp -p 5005:5005 flask-image
docker exec -it flaskapp bash
```

Utilizamos docker-compose:

```bash
docker-compose up --build 
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

## ✨ Test

(venv) python -m pytest --setup-show --cov=apps --cov-report=html

ultimas modificaciones

lanzar test_measures.ipynb para extraer los datos del proyecto de sonar.
Esos datos se transforman y se creand dos nuevos ficheros; historico.csv y metricas.csv

Posteriormente se lanza init_db.py para recrear la bbdd y cargar los csv (historico, metrica y proveedores).

## Formatear el código

La PEP8 es una guía que indica las convenciones estilísticas a seguir para escribir código Python. Se trata de un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.

### Flake8

Flake8 es un linter de tu código. Instalamos la dependencia de flake8

```bash
pip install flake8
```

Luego podemos ejecutar:

```bash
flake8 .\infocodest\  --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
flake8 .\infocodest\ --select F401
```

### Black

Black es una herramienta que le permite identificar errores y formatear su código Python al mismo tiempo.

```bash
pip install black
```

Luego podemos ejecutar:

```bash
# sto comprobará qué archivos Python pueden formatearse en la carpeta actual (pero en realidad no modifica el archivo Python).
black --chech .\infocodes
# Esto muestra lo que hay que hacer con el archivo, pero no lo modifica.
black --check --diff file_name.py
# Para formatear más de un archivo Python, escribir
black .\infocodes
```
