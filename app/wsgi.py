# wsgi.py
"""Python script for TextSuite deployment."""

from app.main import app
from app.config import ProductionConfig


def start():
    """Start flask development server"""
    app.config.from_object(ProductionConfig())
    app.run()


if __name__ == "__main__":
    app.config.from_object(ProductionConfig())
    app.run()
