import pytest
from flask import Flask
from app.__init__ import create_app


@pytest.fixture
def app():
    app = create_app()
    return app