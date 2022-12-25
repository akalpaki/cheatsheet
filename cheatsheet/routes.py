from flask import Blueprint, request
from cheatsheet.model import Repo, CheatSheet
'''
This blueprint contains the routes for the REST API.
General idea: Receive request > Strip data from request >
Pass data to business logic > Return response. 
"GET" methods are specified for clarity, Flask does "GET"
by default if no other method is specified.
'''

api = Blueprint('cheat_sheet', __name__, url_prefix='/cheat_sheet')


@api.route('/')
def get_all():
    """Returns all cheat-sheets for the frontpage."""
    returning_array = []
    a = Repo.get_all()
    for sheet in a:
        returning_array.append(sheet.to_json())
    return returning_array, 200


@api.route('/', methods=['POST'])
def create_sheet():
    """Creates a new cheat-sheet."""
    sheet_data = {
        "author": request.json.get("author"),
        "title": request.json.get("title"),
        "body": request.json.get("body")
    }
    a = Repo.create(sheet_data["author"], sheet_data["title"], sheet_data["body"])
    return a.to_json(), 201


@api.route('/<int:sheet_id>/', methods=['GET'])
def get_sheet(sheet_id):
    """Grabs a cheat-sheet from db."""
    sheet = Repo.get(sheet_id=sheet_id)
    if sheet:
        return sheet, 200
    else:
        return "Page not Found", 404


@api.route('/<int:sheet_id>/', methods=['PUT'])
def update_sheet(sheet_id):
    """Makes a new cheat-sheet."""
    update_data = CheatSheet(sheet_id,
                             request.json.get("author"),
                             request.json.get("title"),
                             request.json.get("body")
                             )
    a = Repo.update(update_data)
    return a.to_json(), 200


@api.route('/<int:sheet_id>/', methods=['DELETE'])
def delete_sheet(sheet_id):
    """Deletes the cheat-sheet."""
    deleted = Repo.delete(sheet_id=sheet_id)
    if deleted:
        return "None", 204
    else:
        return "Failed to delete.", 500
