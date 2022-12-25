from cheatsheet.db import get_db


class CheatSheet:
    """The model class for cheat-sheets"""

    def __init__(self, sheet_id, author, title, body):
        self.id = sheet_id
        self.author = author
        self.title = title
        self.body = body

    def to_json(self):
        return self.__dict__


class CheatSheetManager:
    """Class containing the tools to use CheatSheet."""

    @staticmethod
    def get(sheet_id):
        db = get_db()
        query_result = db.execute("SELECT * FROM cheat_sheet WHERE id = (?)",
                                  (sheet_id,)).fetchone()
        return query_result, 200

    @staticmethod
    def create(author, title, body):
        db = get_db()
        curr = db.cursor()
        curr.execute(
            "INSERT INTO cheat_sheet (author, title, body)"
            "VALUES (?, ?, ?)",
            (author, title, body)
        )
        db.commit()
        sheet_id = curr.lastrowid
        data = CheatSheet(sheet_id, author, title, body)
        return data


    @staticmethod
    def put(sheet_id, title, body):
        get_db().execute("UPDATE cheat_sheet SET title = ?, body = ?"
                         "WHERE id = ?",
                         (title, body, sheet_id)
        )
        get_db().commit()
        return dict(id=sheet_id, message="Cheat-sheet updated!"), 200

    @staticmethod
    def delete(sheet_id):
        get_db().execute("DELETE FROM cheat_sheet WHERE id = ?", (sheet_id,))
        return dict(message="Cheat-sheet deleted."), 204
