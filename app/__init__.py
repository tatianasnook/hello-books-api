from flask import Flask
from .routes.book_routes import bp as books_bp
from .routes.author_routes import bp as author_bp
from .routes.genre_routes import bp as genre_bp
from .db import db, migrate
from .models import book, author, genre, book_genre
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(books_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(genre_bp)

    return app
