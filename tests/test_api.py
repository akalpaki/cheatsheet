import json


def test_get_one_sheet(client):
    response = client.get("/1/")
    data = response.get_json()
    assert response.status_code == 200
    assert data['output']['author'] == "Remis"


def test_get_all_sheets(client):
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
    assert output['body'] == 'test123'
    assert output['created'] == 'now'


def test_create_sheet(client):
    data = json.dumps({
        'author': 'create_test',
        'title': 'test title',
        'body': 'creating a test entry'
    })
    response = client.post(
        '/cheat_sheet/',
        data=data,
        content_type='application/json'
    )
    output = json.loads(response.get_data(as_text=True))
    print(output)
    assert response.status_code == 201
    assert len(output) != 0


def test_delete_sheet(client):
    # Find a way to assert that the object has actually been deleted.
    response = client.delete(
        "/1/",
        content_type='application/json'
    )
    assert response.status_code == 204
