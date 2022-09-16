import mysql.connector
import pymysql
from flask import Flask

from PassGen import config

pymysql.install_as_MySQLdb()

mysql_ = mysql.connector.connect(
    user=config.USER, password=config.PASSWORD, host=config.HOST
)
cursor_ = mysql_.cursor()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        from . import views

        cursor_.execute("CREATE DATABASE IF NOT EXISTS PassGen")
        cursor_.execute(
            "CREATE TABLE IF NOT EXISTS PassGen.accounts (name TEXT ,password TEXT, username TEXT, hint TEXT, last_updated DATETIME, id INT PRIMARY KEY AUTO_INCREMENT)"
        )

        return app
