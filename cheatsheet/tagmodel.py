from cheatsheet.db import get_db


class Tag:

    def __init__(self, tag_id, name, description):
        self.id = tag_id
        self.name = name
        self.description = description


class TagRepo:

    @staticmethod
    def add_tag(name, description):
        pass
