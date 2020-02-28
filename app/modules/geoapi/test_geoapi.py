from flask import url_for
from pytest import approx

def test_point_distance(client):
    response = client.get("/api/v1/geoapi/point/distance/?start_lng=8.83546&start_lat=53.071124&end_lng=10.006168&end_lat=53.549926")
    assert response.status_code == 200
    assert response.json == approx(94.48957)

def test_polygon_area(client):
    payload =   {
                    "type":"Feature",
                    "geometry":{
                        "type":"Polygon",
                        "coordinates":[
                            [
                                13.4197998046875,
                                52.52624809700062
                            ],
                            [
                                13.387527465820312,
                                52.53084314728766
                            ],
                            [
                                13.366928100585938,
                                52.50535544522142
                            ],
                            [
                                13.419113159179688,
                                52.501175722709434
                            ],
                            [
                                13.4197998046875,
                                52.52624809700062
                            ]
                        ]
                    }
                }
    response = client.post("/api/v1/geoapi/polygon/area/",
                           json=payload )
    assert response.status_code == 200
    assert response.json == approx(13351828.06010)

def test_linestring_length(client):
    payload =   {
                    "type":"Feature",
                    "geometry":{
                        "type":"LineString",
                        "coordinates":[
                            [
                                13.420143127441406,
                                52.515594085869914
                            ],
                            [
                                13.421173095703125,
                                52.50535544522142
                            ],
                            [
                                13.421173095703125,
                                52.49532344352079
                            ]
                        ]
                    }
                }
    response = client.post("/api/v1/geoapi/linestring/length/",
                           json=payload )
    assert response.status_code == 200
    assert response.json == approx(2201.13038743)