import pytest
from website import app


@pytest.fixture
def app_():
    """Configuring app for testing session."""
    app.config["TESTING"] = True
    app.config["MAIL_SUPPRESS_SEND"] = True

    yield app


@pytest.fixture
def client(app_):
    """Simulating a test client."""
    return app_.test_client()


@pytest.fixture
def data():
    """Simulating contact form data."""
    form_data = {
        "name": "Jean Dupond",
        "email": "jean.dupond@xmail.com",
        "message": "Ceci est un test",
    }

    return form_data
