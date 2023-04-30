from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.platform import Platform

import repositories.platform_repository as platform_repository

platforms_blueprint = Blueprint("platforms", __name__)

@platforms_blueprint.route("/platforms")
def platforms():
    platforms = platform_repository.select_all()
    return render_template("platforms/home.jinja", platforms = platforms)

@platforms_blueprint.route("/platforms/<id>")
def show(id):
    platform = platform_repository.select(id)
    return render_template("platforms/show.jinja", platform = platform)