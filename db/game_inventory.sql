DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS platforms;


CREATE TABLE platforms (
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(id),
    platform_name VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    stock_level INT,
    buy_price DECIMAL(10, 2),
    sell_price DECIMAL(10, 2),
    platform_id INT REFERENCES platforms(id)
);
