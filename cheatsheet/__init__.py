from flask import Flask, jsonify, make_response

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

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

