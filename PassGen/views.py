from flask import render_template, current_app


@current_app.route("/")
def index():
    return render_template("index.html")
