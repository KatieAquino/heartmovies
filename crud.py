"""CRUD operations for HeartMovies database."""

from model import db, connect_to_db, User, Movie, FavoriteMovie


def create_user(username, email, password):
    """Creates and returns a new user for the database."""

    new_user = User(username=username, email=email)
    
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def create_movie(title, poster, plot):
    """Creates and returns a new movie for the database."""

    new_movie = Movie(title=title, poster=poster, plot=plot)

    db.session.add(new_movie)
    db.session.commit()

    return new_movie


def create_favorite_movie(user_id, movie_id):
    """Creates a new favorite between a user and movie."""

    new_favorite = FavoriteMovie(user_id=user_id, movie_id=movie_id)

    db.session.add(new_favorite)
    db.session.commit()

    return new_favorite


if __name__ == '__main__':
    from server import app
    connect_to_db(app)