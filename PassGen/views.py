from flask import render_template, current_app, url_for, request
from flask_login import logout_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from PassGen import login_manager, db
from PassGen.ctrla import Database
from PassGen.models import User

database = Database()


@login_manager.user_loader
def load_user(id_: int):
    return database.get(User, id_)


@current_app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user = db.session.query(User).filter(User.email == email).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for("index"))
    else:
        return "Login failed."


@current_app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@current_app.route("/signup", methods=["POST"])
def signup():
    _ = User(email=request.form["email"],
             password=generate_password_hash(request.form["password"]))

    database.create(_)
    login_user(_)
    return redirect(url_for("index"))


@current_app.route("/")
def index():
    return render_template("index.html")
