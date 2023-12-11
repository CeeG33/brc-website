import pytest


class TestURLs:
    def test_homepage(self, client):
        """Testing rendering of the home page."""
        response = client.get("/")
        assert b"Welcome to my website !" in response.data
