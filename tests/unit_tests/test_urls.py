import pytest
from website import app, mail, RECIPIENT_MAIL, Message


class TestURLs:
    def test_homepage_get(self, client):
        """Testing rendering of the home page."""
        response = client.get("/")

        assert b"Bienvenue chez BRC" in response.data

    def test_homepage_post(self, client, data, mocker):
        """Testing contact form located in the home page."""
        mocker.patch("website.mail.send")

        response = client.post("/", data=data)

        assert response.status_code == 200
