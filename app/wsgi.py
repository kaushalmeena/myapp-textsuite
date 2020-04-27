# wsgi.py
"""Python script for TextSuite deployment."""

from app.server import app
from app.config import ProductionConfig


def start():
    """Start flask production server"""
    app.config.from_object(ProductionConfig())
    app.run()


if __name__ == "__main__":
    start()
