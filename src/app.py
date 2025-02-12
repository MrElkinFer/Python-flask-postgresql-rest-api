from flask import Flask
from config import configKey
from routes import Movie
from flask_cors import CORS


app = Flask(__name__)
# cors para habilitadar peticiones desde cualquier origen
CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


def page_not_found(error):
    return "<h1>Page not found...</h1>", 404


if __name__ == '__main__':
    app.config.from_object(configKey['development'])
    # blueprints
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    # Manejador de error
    app.register_error_handler(404, page_not_found)
    app.run()
