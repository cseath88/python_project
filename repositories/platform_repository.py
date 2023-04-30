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