import os

MYSQL_DATABASE_DB = os.environ.get('MYSQL_DATABASE_DB', 'python_crud_pessoas')
MYSQL_DATABASE_USER = os.environ.get('MYSQL_DATABASE_USER', 'root')
MYSQL_DATABASE_PASSWORD = os.environ.get('MYSQL_DATABASE_PASSWORD', None)
MYSQL_DATABASE_HOST = os.environ.get('MYSQL_DATABASE_HOST', 'localhost')

# FLASK_APP = 'python_crud_pessoas'
FLASK_ENV = os.environ.get("APP_ENV", "development")

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = os.environ.get("PORT", 5000)
SITE_URL = os.environ.get("SITE_URL", "http://127.0.0.1:5000")

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(APP_FOLDER, "static")
TEMPLATES_FOLDER = os.path.join(APP_FOLDER, "templates")

DEBUG = True
TEMPLATES_AUTO_RELOAD = True