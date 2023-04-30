from flask import Flask, render_template

from controllers.game_controller import games_blueprint
from controllers.platform_controller import platforms_blueprint


app = Flask(__name__)

app.register_blueprint(games_blueprint)
app.register_blueprint(platforms_blueprint)

@app.route('/')
def home():
    return render_template('home.jinja')

if __name__ == '__main__':
    app.run(debug=True)