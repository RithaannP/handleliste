DROP TABLE IF EXISTS handleliste;

DROP TABLE IF EXISTS produkt;

CREATE TABLE produkt (
    id INTEGER,
    navn TEXT NOT NULL UNIQUE,
    kategori TEXT NOT NULL CHECK (kategori IN ('Essentials', 'Diverse')),
    trengs INTEGER NOT NULL DEFAULT 0 CHECK (trengs IN (0, 1)),
    antall INTEGER NOT NULL DEFAULT 1 CHECK (antall > 0),
    PRIMARY KEY (id)
);