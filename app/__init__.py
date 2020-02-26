# encoding: utf-8
"""
Example RESTful API Server.
"""
from flask import Flask
from flask_restplus import Resource, Api


api_v1 = Api(
    version='1.0',
    title="LlactaLab | REST GeoAPI",
    description=(
        "This is a REST API with geospatial super power.\n\n"
        "Checkout more at https://llactalab.ucuenca.edu.ec\n"
    ),
)

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    app = Flask(__name__, **kwargs)

    # Load the config file
    app.config.from_object('config.DevelopmentConfig')

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Initialize the modules
    from . import modules
    modules.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    # Return the app to the runner state so it gets actually loaded.
    #app.run(host='127.0.0.1', port='5000')
    app.run(debug=True, port=5000)