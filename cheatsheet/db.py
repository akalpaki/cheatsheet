import sqlite3

import click
from flask import g, current_app

# This is the database setup file.


def get_db():
    """Creates the database connection."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Closes the db after a transaction is done."""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """Initializes the database for a transaction."""
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode("utf8"))


@click.command('init-db')
def init_db_command():
    """Clear existing data, create new tables."""
    init_db()
    click.echo('Database initialized.')


def init_app(app):
    """Registers the db. Makes sure no transaction is
    running, then initializes the db for new transaction."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
