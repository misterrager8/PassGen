import datetime

import click
import pyperclip

from PassGen import config, create_app, db
from PassGen.models import Account

app = create_app(config)


@click.group()
def cli():
    """PassGen - password manager app"""
    pass


@cli.command()
def list_all():
    """List all accounts"""
    with app.app_context():
        for i in Account.query.all():
            click.secho("[%s] %s" % (i.id, i.name), fg="cyan")


@cli.command()
@click.argument("name")
def add_account(name):
    """Add an account with NAME"""
    password = input(f"Enter password for {name}: ")
    with app.app_context():
        account_ = Account(
            name=name, password=password, last_updated=datetime.datetime.now()
        )
        db.session.add(account_)
        db.session.commit()

    click.secho("Account added", fg="green")


@cli.command()
@click.argument("id")
def delete_account(id):
    """Delete account with ID"""
    with app.app_context():
        account_ = Account.query.get(int(id))
        db.session.delete(account_)
        db.session.commit()

    click.secho("Account deleted.", fg="green")


@cli.command()
@click.argument("id")
def copy_pass(id):
    """Copy account password with ID to clipboard"""
    with app.app_context():
        account_ = Account.query.get(int(id))
        pyperclip.copy(account_.password)

    click.secho("Password copied.", fg="green")


@cli.command()
def web():
    """Launch web interface"""
    app.run()
