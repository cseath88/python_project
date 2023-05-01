from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.platform import Platform

import repositories.platform_repository as platform_repository
import repositories.game_repository as game_repository

platforms_blueprint = Blueprint("platforms", __name__)

@platforms_blueprint.route("/platforms")
def platforms():
    platforms = platform_repository.select_all()
    return render_template("platforms/home.jinja", platforms = platforms)

@platforms_blueprint.route("/platforms/<id>")
def show(id):
    platforms = platform_repository.select(id)
    games = game_repository.select_all()
    return render_template("platforms/show.jinja", platforms = platforms, games = games)