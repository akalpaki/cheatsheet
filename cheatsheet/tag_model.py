from cheatsheet.db import get_db


class Tag:
    """Model class for tags used by cheat-sheets."""
    def __init__(self, tag_id, name, description):
        self.id = tag_id
        self.name = name
        self.description = description


class TagRepo:
    """Repository of tag tools."""
    @staticmethod
    def find_tag(tag_id):
        """Query db if the tag exists, return bool."""
        pass

    @staticmethod
    def add_tag(name, description):
        """Adds a new tag to the db."""
        pass

    @staticmethod
    def update_tag(name, description):
        """Update a tag to change name and add/change description."""
        pass

    @staticmethod
    def delete_tag(tag_id):
        """Delete a tag FROM THE DATABASE.
        FOR INTERNAL/TESTING PURPOSES!!!"""
        pass

    @staticmethod
    def remove_sheet_tag(sheet_id, tag_id):
        """Removes a tag from a cheat-sheet."""
        pass

    @staticmethod
    def retrieve_desc(tag_id):
        """Retrieves a description for a tag.
        Use case: mouse hover a tag -> retrieve and display the description of the tag."""
        pass
