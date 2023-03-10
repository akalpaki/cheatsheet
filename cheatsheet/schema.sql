DROP TABLE IF EXISTS cheat_sheet;
DROP TABLE IF EXISTS tag;

CREATE TABLE cheat_sheet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    body TEXT NOT NULL,
    tags TEXT
);


CREATE TABLE tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);