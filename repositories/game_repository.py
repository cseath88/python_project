from db.run_sql import run_sql

from models.game import Game
from models.platform import Platform

import repositories.platform_repository as platform_repository

def save(game):
    sql = "INSERT INTO games (title, description, stock_level, buy_price, sell_price, platform_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [game.title, game.description, game.stock_level, game.buy_price, game.sell_price, game.platform.id]
    results = run_sql(sql, values)
    game.id = results[0]['id']
    return game


def select_all():
    games = [ ]
    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        game = Game(row['title'], row['description'], row['stock_level'], row['buy_price'], row['sell_price'], row['platform_id'], row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        game = Game(result['title'], result['description'], result['stock_level'], result['buy_price'], result['sell_price'], result['platform_id'], result['id'])
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def platform(game):
    platform = [ ]
    sql = "SELECT * FROM platforms WHERE game_id = %s"
    values = [game.id]
    results = run_sql(sql, values)

    for row in results:
        platform = Platform(row['name'], row['id'])
        platform.append(platform)
    return platform

def update(game):
    sql = "UPDATE games SET (title, description, stock_level, buy_price, sell_price, platform_id) = (%s, %s, %s,%s, %s, %s) WHERE id = %s"
    values = [game.title, game.description, game.stock_level, game.buy_price, game.sell_price, game.platform.id, game.id]
    run_sql(sql, values)