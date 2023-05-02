from db.run_sql import run_sql

from models.game import Game
from models.platform import Platform

import repositories.game_repository as game_repository

def save(platform):
    sql = "INSERT INTO platforms (platform_name) VALUES (%s) RETURNING *"
    values = [platform.platform_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    platform.id = id
    return platform

def select_all():
    platforms = [ ]
    sql = "SELECT * FROM platforms"
    results = run_sql(sql)
    for row in results:
        platform = Platform(row['platform_name'], row['id'])
        platforms.append(platform)
    return platforms

def select(id):
    platform = None
    sql = "SELECT * FROM platforms WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        platform = Platform(result['platform_name'], result['id'])
    return platform

def delete_all():
    sql = "DELETE FROM platforms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# This function is for getting the platform ID for a game so I can display it on the Platform page
def game_platform(platform):
    game_platform = [ ]
    sql = "SELECT * FROM games WHERE platform_id = %s"
    values = [platform.id]
    results = run_sql(sql, values)

    for row in results:
        game = Game(row['title'], row['description'], row['stock_level'], row['buy_price'], row['sell_price'],row['platform_id'], row['id'])
        game_platform.append(game)
    return game_platform


