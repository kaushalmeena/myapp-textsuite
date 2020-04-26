# wsgi.py
"""Python script for TextSuite deployment."""

from app.server import app


def start():
    """Start flask production server"""
    app.config.from_object('app.config.ProductionConfig')
    app.run()


if __name__ == "__main__":
    start()
