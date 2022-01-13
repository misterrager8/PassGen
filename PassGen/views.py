from flask import render_template, current_app

from PassGen import login_manager
from PassGen.ctrla import Database
from PassGen.models import User

database = Database()


@login_manager.user_loader
def load_user(id_: int):
    return database.get(User, id_)


@current_app.route("/")
def index():
    return render_template("index.html")
