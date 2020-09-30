import pytest
from connector import create_app


@pytest.fixture
def app():
    app = create_app("connector.config.TestConfig")

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
