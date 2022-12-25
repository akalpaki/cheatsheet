from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = False
DEBUG = True
FLASK_ENV = environ.get('FLASK_ENV')
SECRET_KEY = environ.get('SECRET_KEY')
DATABASE = "./instance/cheatsheet.sqlite"
