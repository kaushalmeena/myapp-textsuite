"""Contains app factory for TextSuite."""

from flask import Flask

from textsuite.extensions import compress


def create_app(app_config):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config)

    # Initialize plugins
    compress.init_app(app)

    with app.app_context():
        from textsuite.routes import app_blueprint

        # Register blueprints
        app.register_blueprint(app_blueprint)

        return app
