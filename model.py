"""Database for HeartMovies"""

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User in the HeartMovies database."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128))

    # hash password for database security
    def set_password(self, password):
        """Hashes a users password for added security."""

        self.password = generate_password_hash(password)
    

    def check_password(self, password):
        """Checks a password entered to see if it matches the hashed password."""

        return check_password_hash(self.password, password)


    def __repr__(self):
        """Cleaner representation of user for ease of use."""

        return f'<User id={self.id}, username={self.username}, email={self.email}>'


class Movie(db.Model):
    """Movie in the HeartMovies database."""

    __tablename__ = 'movies'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    poster = db.Column(db.Text)
    plot = db.Column(db.Text)


    def __repr__(self):
        """Cleaner representation of a movie for ease of use."""

        return f'<Movie id={self.id}, title={self.title}>'


class FavoriteMovie(db.Model):
    """Favorited movie assigned to a user."""

    __tablename__ = 'favorites'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    user = db.relationship('User', backref='users')
    movie = db.relationship('Movie', backref='movies')


    def __repr__(self):
        """Cleaner represenation of a favorite for ease of use."""

        return f'<FavoriteMovie id={self.id}, user={sel
f.user.username}, movie={self.movie.title}>'

def connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True):
    """Connects app to database."""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)
    
    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print('Connected to db!')