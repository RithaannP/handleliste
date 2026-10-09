DROP TABLE IF EXISTS handleliste;

CREATE TABLE handleliste (
    id INTEGER,
    navn TEXT NOT NULL,
    antall INTEGER CHECK( antall > 0),
    PRIMARY KEY(id)
);