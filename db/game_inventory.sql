DROP TABLE IF EXISTS platforms CASCADE;
DROP TABLE IF EXISTS games CASCADE;

CREATE TABLE platforms (
    id SERIAL PRIMARY KEY,
    platform_name VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    stock_level INT,
    buy_cost DECIMAL(10, 2),
    sell_price DECIMAL(10, 2),
    platform_id INT REFERENCES platforms(id)
);
