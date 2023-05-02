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
    platform = platform_repository.select(id)
    games = platform_repository.game_platform(platform)
    return render_template("platforms/show.jinja", platform = platform, games = games)

@platforms_blueprint.route("/platforms/new", methods=['GET'])
def add_new_platform():
    platforms = platform_repository.select_all()
    return render_template("platforms/new.jinja", platforms = platforms)

@platforms_blueprint.route("/platforms", methods=['POST'])
def post_new_platform():
    platform_name = request.form['platform_name']
    platform = Platform(platform_name)
    platform_repository.save(platform)