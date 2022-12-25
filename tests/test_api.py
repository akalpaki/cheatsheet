import json


def test_get_one_sheet(client):
    response = client.get("/1/")
    data = response.get_json()
    assert response.status_code == 200
    assert data['output']['author'] == "Remis"


def test_get_all_sheets(client):
    response = client.get("/cheat_sheet/")
    data = response.get_json()
    assert len(data) != 0


def test_edit_sheet(client):
    data = json.dumps({
        'id': 9,
        'author': 'test',
        'title': 'updated title',
        'body': 'test123'
    })
    response = client.put(
        "/cheat_sheet/9/",
        data=data,
        content_type='application/json'
    )
    output = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert output['title'] == 'updated title'
    assert output['body'] == 'test123'


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
    temp_sheet = client.post(
        '/cheat_sheet/',
        data=json.dumps({
            'author': 'Test',
            'title': 'Deletion Test',
            'body': 'I shouldnt exist'
        }),
        content_type='application/json'
    )
    temp_sheet_id = temp_sheet.json.get('id')
    deleted = client.delete(
        f'/cheat_sheet/{temp_sheet_id}/',
        content_type='application/json'
    )
    assert deleted.status_code == 204
    a = client.get(
        f'/cheat_sheet/{temp_sheet_id}/',
        content_type='application/json'
    )
    assert a.status_code == 404
