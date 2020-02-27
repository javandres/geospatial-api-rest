import pytest
from flask import Flask
from app.__init__ import create_app


@pytest.fixture
def app():
    app = create_app()
    return app




# import pytest
# from app.__init__ import create_app

# myapp = create_app()
# print(myapp)
# # Creates a fixture whose name is "app"
# # and returns our flask server instance
# @pytest.fixture
# def app():
#     app = create_app()
#     a = 0 / 1
#     #app = {}
#     return app


# import pytest
# from flask import Flask
# from app import initialize_app


# @pytest.fixture
# def app():
#     app = Flask(__name__)
#     initialize_app(app)
#     return app    