from flask import render_template, current_app, request, redirect, url_for
from PassGen.models import Account
from PassGen import db
import datetime


@current_app.route("/")
def index():
    return render_template("index.html", accounts=Account.query.all())


@current_app.route("/create_account", methods=["POST"])
def create_account():
    account_ = Account(
        name=request.form["name"],
        username=request.form["username"],
        password=request.form["password"],
        hint=request.form["hint"],
        last_updated=datetime.datetime.now(),
    )
    db.session.add(account_)
    db.session.commit()

    return redirect(request.referrer)


@current_app.route("/edit_account", methods=["POST"])
def edit_account():
    account_ = Account.query.get(int(request.args.get("id_")))

    account_.name = request.form["name"]
    account_.username = request.form["username"]
    account_.hint = request.form["hint"]
    if account_.password != request.form["password"]:
        account_.last_updated = datetime.datetime.now()
    account_.password = request.form["password"]

    db.session.commit()

    return redirect(request.referrer)


@current_app.route("/delete_account")
def delete_account():
    account_ = Account.query.get(int(request.args.get("id_")))
    db.session.delete(account_)
    db.session.commit()

    return redirect(request.referrer)


@current_app.route("/export_all")
def export_all():
    return "\n".join(
        [
            "%s,%s,%s,%s,%s" % (i.name, i.username, i.password, i.hint, i.last_updated)
            for i in Account.query.all()
        ]
    )
