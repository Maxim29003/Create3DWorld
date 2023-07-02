import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
PORT = 8100

SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
