from flask import Blueprint, render_template, request

'''
This blueprint contains the routes for the REST API.
General idea: Receive request > Strip data from request >
Pass data to business logic > Return response. 
"GET" methods are specified for clarity, Flask does "GET"
by default if no other method is specified.
'''

api = Blueprint('cheat_sheet', __name__, url_prefix='/cheat_sheet')


@api.route('/')
def frontpage():
    """Loads the frontpage."""
    return render_template('index.html')


@api.route('/', methods=['POST'])
def create_sheet():
    """Creates a new cheat-sheet."""
    sheet_data = {
        "author": request.json.get("author"),
        "body": request.json.get("body")
    }
    # Call business func that feeds sheet_data to db
    pass


@api.route('/<int:sheet_id>/', methods=['GET'])
def get_sheet(sheet_id):
    """Grabs a cheat-sheet from db."""
    # Grab the sheet with id = sheet_id from db,
    # Probably render template with the requested sheet_data
    pass


@api.route('/<int:sheet_id>/', methods=['PUT'])
def update_sheet(sheet_id):
    """Makes a new cheat-sheet."""
    update_data = {
        "body": request.json.get("body")
    }
    # Call business func that feeds update_data to
    # data access func which updates db entry
    pass


@api.route('/<int:sheet_id>/', methods=['DELETE'])
def delete_sheet(sheet_id):
    """Deletes the cheat-sheet."""
    # Call business func that asks data access func to delete
    # db entry with id = sheet_id.
    pass
