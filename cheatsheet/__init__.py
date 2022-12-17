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
        "body": "This is also a standin for a cheat sheet.",
        "created": "2 days ago"
    }
]


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        pass
        #app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def hello():
        output = [sheet for sheet in cheat_list]
        return jsonify(output)

    @app.route("/<int:sheet_id>/", methods=['GET'])
    def get_sheet(sheet_id):
        output = [sheet for sheet in cheat_list if sheet["id"] == sheet_id]
        a = jsonify({'output': output[0]})
        response = make_response(a)
        response.headers["Content-Type"] = 'application/json; charset=utf-8'
        return response

    @app.route("/<int:sheet_id>/", methods=['PUT'])
    def update_sheet(sheet_id):
        changing_sheet = [sheet for sheet in cheat_list if sheet["id"] == sheet_id]
        changing_sheet[0]['author'] = request.json.get('author', changing_sheet[0]['author'])
        changing_sheet[0]['body'] = request.json.get('body', changing_sheet[0]['body'])
        changing_sheet[0]['created'] = request.json.get('created', changing_sheet[0]['created'])
        b = jsonify(changing_sheet[0])
        return b

    @app.route("/<int:sheet_id>/", methods=['DELETE'])
    def delete_sheet(sheet_id):
        del cheat_list[0][f"{sheet_id}"]
        return cheat_list

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

