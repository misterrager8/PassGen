import datetime

import click
import pyperclip

from PassGen import config, create_app
from PassGen.models import Account


@click.group()
def cli():
    """PassGen - password manager app"""
    pass


@cli.command()
def list_all():
    """List all accounts"""
    for i in Account.all():
        click.secho("[%s] %s" % (i.id, i.name), fg=config.CLI_COLOR)


@cli.command()
@click.option("--name", "-n", prompt=True)
@click.option("--password", "-p", prompt=True, hide_input=True)
def add_account(name, password):
    """Add an account with NAME"""
    account_ = Account(
        name=name, password=password, last_updated=datetime.datetime.now()
    )
    account_.insert()

    click.secho("Account added", fg=config.CLI_COLOR)


@cli.command()
@click.option("--id", "-i", prompt=True, type=int)
def delete_account(id):
    """Delete account with ID"""
    account_ = Account.get(int(id))
    account_.delete()

    click.secho("Account deleted.", fg=config.CLI_COLOR)


@cli.command()
@click.option("--id", "-i", prompt=True, type=int)
def copy_pass(id):
    """Copy account password with ID to clipboard"""
    account_ = Account.get(int(id))
    pyperclip.copy(account_.password)

    click.secho("Password copied.", fg=config.CLI_COLOR)


@cli.command()
@click.option("--id", "-i", prompt=True, type=int)
@click.option("--password", "-p", prompt=True, hide_input=True)
def change_pass(id, password):
    """Change account password with ID"""
    account_ = Account.get(int(id))
    account_.password = password
    account_.last_updated = datetime.datetime.now()
    account_.edit()

    click.secho("Password changed.", fg=config.CLI_COLOR)


@cli.command()
def web():
    """Launch web interface"""
    app = create_app(config)
    app.run()
