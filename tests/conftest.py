import pytest
from cheatsheet.__init__ import create_app
import cheatsheet.db


@pytest.fixture()
def app():
    app = create_app(current_config="testing")

    with app.app_context():
        cheatsheet.db.init_app(app)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
