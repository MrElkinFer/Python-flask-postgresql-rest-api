from flask import Blueprint, jsonify, request
from models.MovieModel import MovieModel
import uuid
from models.entities.Movie import Movie

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)})


@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)})


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        id = str(uuid.uuid4())
        movie = Movie(id, title, duration, released)
        affectedRows = MovieModel.add_movie(movie)
        if affectedRows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'Message: ': "Error on Insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)})


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(id, title, duration, released)
        affectedRows = MovieModel.update_movie(movie)
        if affectedRows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'Message: ': "No  movie Updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)})


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)
        affectedRows = MovieModel.delete_movie(movie)
        if affectedRows == 1:
            return jsonify({'Message: ': "Movie deleted.."})
        else:
            return jsonify({'Message: ': "Error on Insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)})
