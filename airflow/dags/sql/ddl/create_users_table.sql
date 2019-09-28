CREATE TABLE IF NOT EXISTS {{ params.prefix }}_users (
    id integer PRIMARY KEY,
    name text NOT NULL,
    email name text NOT NULL
);
