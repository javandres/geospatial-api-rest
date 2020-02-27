from flask import url_for

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
    assert response.json == 13351828.060103219

def test_point_distance(client):
    response = client.get("/api/v1/geoapi/point/distance/?start_lng=8.83546&start_lat=53.071124&end_lng=10.006168&end_lat=53.549926")
    assert response.status_code == 200
    assert response.json == 94.48957157194933