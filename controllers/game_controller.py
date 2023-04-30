from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.game import Game

import repositories.game_repository as game_repository

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/home.jinja", title = "Games", games = games)

@games_blueprint.route("/games/<id>")
def show(id):
    game = game_repository.select(id)
    return render_template("games/show.jinja", game = game)