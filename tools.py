
import sqlite3
import json


# Function 1: Show All Movies
def showAllMovies() -> str:
    """Show all movies with their multiplex and hall details."""

    conn = sqlite3.connect("movieDB.sqlite3")
    cursor = conn.cursor()

    query = """
    SELECT Movie.movie_id, Movie.genre, Movie.time,
           Hall.hall_id, Multiplex.multiplex_id
    FROM Movie
    JOIN Hall ON Movie.movie_id = Hall.movie_id
    JOIN Multiplex ON Hall.hall_id = Multiplex.hall_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()

    return json.dumps(data)


# Function 2: Show Movies By Multiplex
def showMoviesByMultiplex(multiplex_id: int) -> str:
    """
    Show movies by multiplex ID.

    Args:
        multiplex_id: Integer ID of the multiplex.
    """

    conn = sqlite3.connect("movieDB.sqlite3")
    cursor = conn.cursor()

    query = """
    SELECT Movie.movie_id, Movie.genre, Movie.time,
           Hall.hall_id, Multiplex.multiplex_id
    FROM Movie
    JOIN Hall ON Movie.movie_id = Hall.movie_id
    JOIN Multiplex ON Hall.hall_id = Multiplex.hall_id
    WHERE Multiplex.multiplex_id = ?
    """

    cursor.execute(query, (multiplex_id,))
    data = cursor.fetchall()

    conn.close()

    return json.dumps(data)


# Function 3: Show Movies By Genre
def showMovieByGenre(genre: str) -> str:
    """
    Show movies by genre.

    Args:
        genre: Movie genre such as Action, Comedy or Horror.
    """

    conn = sqlite3.connect("movieDB.sqlite3")
    cursor = conn.cursor()

    query = """
    SELECT Movie.movie_id, Movie.genre, Movie.time,
           Hall.hall_id, Multiplex.multiplex_id
    FROM Movie
    JOIN Hall ON Movie.movie_id = Hall.movie_id
    JOIN Multiplex ON Hall.hall_id = Multiplex.hall_id
    WHERE LOWER(Movie.genre) = LOWER(?)
    """

    cursor.execute(query, (genre,))
    data = cursor.fetchall()

    conn.close()

    return json.dumps(data)
