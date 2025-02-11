from database.bd import get_connection
from .entities.Movie import Movie


class MovieModel():

    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie ORDER BY title ASC")
                resulset = cursor.fetchall()

                for row in resulset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_movie(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie WHERE id= %s", (id,))
                row = cursor.fetchone()

                movie = None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)
