CREATE TABLE IF NOT EXISTS {{ params.prefix }}_addresses (
    id integer PRIMARY KEY,
    user_id integer NOT NULL,
    country text NOT NULL,
    city text NOT NULL,
    zip_code text NOT NULL,
    address text NOT NULL,
    notes text,
    FOREIGN KEY (user_id) REFERENCES {{ params.prefix }}_users (id)
);
