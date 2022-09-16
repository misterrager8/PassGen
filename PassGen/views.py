import datetime
import os
from pathlib import Path

from flask import current_app, redirect, render_template, request

from PassGen.models import Account


@current_app.route("/")
def index():
    return render_template("index.html", accounts=Account.all())


@current_app.route("/add_account", methods=["POST"])
def add_account():
    account_ = Account(
        name=request.form["name"],
        password=request.form["password"],
        last_updated=datetime.datetime.now(),
    )
    account_.insert()

    return redirect(request.referrer)


@current_app.route("/edit_account", methods=["POST"])
def edit_account():
    account_ = Account.get(int(request.args.get("id_")))
    account_.name = request.form["name"]
    account_.username = request.form["username"]
    account_.hint = request.form["hint"]
    account_.last_updated = (
        datetime.datetime.now()
        if account_.password != request.form["password"]
        else account_.last_updated
    )
    account_.password = request.form["password"]

    account_.edit()

    return redirect(request.referrer)


@current_app.route("/delete_account")
def delete_account():
    account_ = Account.get(int(request.args.get("id_")))
    account_.delete()

    return redirect(request.referrer)


@current_app.route("/export_accounts")
def export_accounts():
    export_path = Path(os.getcwd()) / "passgen.txt"
    with open(export_path, "w") as f:
        for i in Account.all():
            f.write(f"{i.name},{i.username or ''},{i.password}\n")

    return f"Exported to {export_path}"
