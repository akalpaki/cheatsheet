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


class CSRepo:
    """Class containing the tools to use CheatSheet."""

    @staticmethod
    def get(sheet_id):
        db = get_db()
        query_result = db.execute("SELECT * FROM cheat_sheet WHERE id = ?",
                                  (sheet_id,)).fetchone()
        if query_result is not None:
            a = CheatSheet(query_result["id"],
                           query_result['author'],
                           query_result['title'],
                           query_result['body']
                           )
            return a
        else:
            return None

    @staticmethod
    def get_all():
        query_array = []
        db = get_db()
        query_result = db.execute("SELECT * FROM cheat_sheet").fetchall()
        for result in query_result:
            query_array.append(CheatSheet(result["id"],
                                          result["author"],
                                          result["title"],
                                          result["body"]
                                          )
                               )
        return query_array

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
    def update(cheat_sheet):
        get_db().execute("UPDATE cheat_sheet SET title = ?, body = ?"
                         "WHERE id = ?",
                         (cheat_sheet.title, cheat_sheet.body, cheat_sheet.id)
        )
        get_db().commit()
        outbound = CSRepo.get(sheet_id=cheat_sheet.id)
        return outbound

    @staticmethod
    def delete(sheet_id):
        db = get_db()
        d = db.execute("DELETE FROM cheat_sheet WHERE id = ?", (sheet_id,))
        db.commit()

        return d.rowcount > 0
