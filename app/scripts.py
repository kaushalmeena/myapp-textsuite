"""Contains scripts to be run by poetry."""

from app.config import DevelopmentConfig, ProductionConfig
from app.main import app


def start_dev():
    """Start TextSuite app in development mode."""
    app.config.from_object(DevelopmentConfig())
    app.run()


def start_prod():
    """Start TextSuite app in production mode."""
    app.config.from_object(ProductionConfig)
    app.run()
