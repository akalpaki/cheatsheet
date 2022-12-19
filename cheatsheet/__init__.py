import os

from flask import Flask, jsonify, make_response, request

cheat_list = [
    {
        "id": 1,
        "author": "Remis",
        "body": "A stand in for a cheat sheet body.",
        "created": "today"
    },
    {
        "id": 2,
        "author": "Alex",
        "body": "This is also a stand in for a cheat sheet.",
        "created": "2 days ago"
    }
]


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'cheatsheet.sqlite')
        )
    else:
        app.config.from_mapping(test_config)

    # This ensures the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Move the routes to a "Routes" module
    # Point of routes: strip the data from the request, pass it to business layer.
    @app.route("/")
    def frontpage():
        output = [sheet for sheet in cheat_list]
        return jsonify(output)

    @app.route("/", methods=['POST'])
    def create_sheet():
        construct_new_entry = dict()
        construct_new_entry.update({"id": len(cheat_list)})
        construct_new_entry.update({
            'author': request.json.get('author'),
            'body': request.json.get('body'),
            'created': request.json.get('created'),
        })
        cheat_list.append(construct_new_entry)
        return cheat_list, 201

    @app.route("/<int:sheet_id>/", methods=['GET'])
    def get_sheet(sheet_id):
        output = [sheet for sheet in cheat_list if sheet["id"] == sheet_id]
        a = jsonify({'output': output[0]})
        response = make_response(a)
        response.headers["Content-Type"] = 'application/json; charset=utf-8'
        return response

    @app.route("/<int:sheet_id>/", methods=['PUT'])
    def update_sheet(sheet_id):
        # author = request.json.get('author')
        # logic.update_sheet(sheet_id, author, body, created)
        changing_sheet = [sheet for sheet in cheat_list if sheet["id"] == sheet_id]
        changing_sheet[0]['author'] = request.json.get('author', changing_sheet[0]['author'])
        changing_sheet[0]['body'] = request.json.get('body', changing_sheet[0]['body'])
        changing_sheet[0]['created'] = request.json.get('created', changing_sheet[0]['created'])
        b = jsonify(changing_sheet[0])
        return b

    @app.route("/<int:sheet_id>/", methods=['DELETE'])
    def delete_sheet(sheet_id):
        cheat_list.pop(sheet_id - 1)
        return cheat_list, 204

    from . import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
