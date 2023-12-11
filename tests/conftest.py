import pytest
from website import app


@pytest.fixture
def app_():
    """Configuring app for testing session."""
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture
def client(app_):
    """Simulating a test client."""
    return app_.test_client()
