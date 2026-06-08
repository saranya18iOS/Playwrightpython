from pathlib import Path
import json

def test_get_user(api_client):

    response = api_client.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "Bret"
    assert "email" in data


def get_root():
    return Path(__file__).resolve().parents[2]

def test_create_post(api_client):

    file_path = get_root() / "test_data" / "api" / "post_payload.json"

    with open(file_path) as file:
        payload = json.load(file)

    response = api_client.post("/posts", payload)

    assert response.status == 201