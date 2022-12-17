import json


def test_request_example(client):
    response = client.get("/1/")
    data = response.get_json()
    assert response.status_code == 200
    assert data['output']['author'] == "Remis"


def test_list(client):
    response = client.get("/")
    data = response.get_json()
    assert len(data) != 0


def test_edit_sheet(client):
    data = json.dumps({
        'id': 1,
        'author': 'test',
        'body': 'test123',
        'created': 'now'
    })
    response = client.put(
        "/1/",
        data=data,
        content_type='application/json'
    )
    output = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert output['author'] == 'test'

