from db.run_sql import run_sql

from models.game import Game
from models.platform import Platform

import repositories.platform_repository as platform_repository

def save(game):
    sql = "INSERT INTO games (title, description, stock_level, buy_cost, sell_price, platform_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [game.title, game.description, game.stock_level, game.buy_cost, game.sell_price, game.platform.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game


def select_all():
    games = [ ]
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        game = Game(row['title'], row['description'], row['stock_level'], row['buy_cost'], row['sell_price'], row['platform_id'], row['id'])
        games.append(game)
    return games