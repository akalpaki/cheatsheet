import pytest
from cheatsheet.__init__ import create_app


@pytest.fixture()
def app():
    app = create_app({
        'TESTING': True,
        #'DATABASE': db_path, add fake db on configtest later
     })

    with app.app_context():
        pass

    yield app

    #os.close(db_fd)
    #os.unlink(db_path)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()