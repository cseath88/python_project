from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.game import Game
from models.platform import Platform

import repositories.game_repository as game_repository
import repositories.platform_repository as platform_repository

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/home.jinja", title = "Games", games = games)

@games_blueprint.route("/games/<id>")
def show(id):
    games = game_repository.select(id)
    return render_template("games/show.jinja", games = games)

@games_blueprint.route("/games/new", methods=['GET'])
def add_new_game():
    games = game_repository.select_all()
    platforms = platform_repository.select_all()
    return render_template("games/new.jinja", games = games, platforms = platforms)

@games_blueprint.route("/games",  methods=['POST'])
def post_new_game():
    platform  = platform_repository.select(request.form['platform_id'])
    title = request.form['title']
    description = request.form['description']
    stock_level = request.form['stock_level']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    game = Game(title, description, stock_level, buy_price, sell_price, platform)
    game_repository.save(game)
    return redirect('/games')

