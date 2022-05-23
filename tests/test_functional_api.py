from fastapi.testclient import TestClient
from beerlog.api import api

client = TestClient(api)

def test_create_beer_via_api():
    response = client.post(
        "/beers",
        json={
            # payload
            "name": "Colorado",
            "style": "IPA",
            "flavor": 3,
            "image": 6,
            "cost": 1,
        },
    )
    assert response.status_code == 201
    result = response.json()
    assert result["name"] == "Colorado"
    assert result["id"] == 1
