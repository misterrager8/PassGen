import os

import dotenv

dotenv.load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("db_url")
SECRET_KEY = os.getenv("secret_key")
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = os.getenv("debug")
ENV = os.getenv("flask_env")
