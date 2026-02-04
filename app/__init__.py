from flask import Flask
from .config import Config
from .extensions import db, jwt, migrate
from .routes.auth import auth_bp
from .routes.users import user_bp
from .errors import register_error_handlers
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    register_error_handlers(app)
    return app
