from cheatsheet.db import get_db


class CheatSheet:
    """The model class for cheat-sheets"""

    def __init__(self, sheet_id, author, title, body, created):
        self.id = sheet_id
        self.author = author
        self.title = title
        self.body = body
        self.created = created  # created needs to be a datetime object


class GetCheatSheet(CheatSheet):
    """Class which contains GET method functionality."""

    def get(self) -> tuple[dict, int]:
        db = get_db()
        request_data = db.execute('SELECT * FROM cheat_sheet WHERE id = ? ',
                                  (CheatSheet.id,)).fetchone()
        return dict(request_data=request_data, message="Success"), 200


class PutCheatSheet(CheatSheet):
    """Class which contains PUT method functionality."""
    def put(self, sheet_id, author, title, body, created):
        db = get_db()
        request_data = CheatSheet(sheet_id, author, title, body, created)
        new_db_entry = db.execute('INSERT INTO cheat_sheet VALUES (?, ?, ?, ?, ?)',
                                  (request_data,))
        return dict(id=new_db_entry.id, message="Cheat-sheet added"), 202

