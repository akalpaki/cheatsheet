import json

def test_request_example(client):
    response = client.get("/1/")
    data = response.get_json()
    assert response.status_code == 200
    assert data['output']['author'] == "Remis"


def test_list(client):
    response = client.get("/")
    data = response.get_json()
    assert len(data) !=

def test_add_sheet(client):
    response = client.post(
        "/add/",
        json.dumps({'id': 3, 'author': 'test', ''})
    )
