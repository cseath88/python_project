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

