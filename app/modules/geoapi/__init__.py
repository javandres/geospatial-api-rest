# encoding: utf-8

from app import api_v1


class GeoApiNamespace:
    namespace = "geoapi"
    description = "GeoAPI"


def init_app(app, **kwargs):
    """
    Init the GeoAPI module.
    """

    # Load the underlying module
    from . import resources

    api_v1.add_namespace(resources.api)