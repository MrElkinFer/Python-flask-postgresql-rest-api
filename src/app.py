from flask import Flask
from config import configKey


app = Flask(__name__)


def page_not_found(error):
    return "<h1>Page not found...</h1>", 404


if __name__ == '__main__':
    app.config.from_object(configKey['development'])
    # Manejador de error
    app.register_error_handler(404, page_not_found)
    app.run()
