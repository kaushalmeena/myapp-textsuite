# wsgi.py
"""Python script for TextSuite deployment."""

from textsuite.server import app


def start():
    """Start flask production server"""
    app.config.from_object('textsuite.config.ProductionConfig')
    app.run()


if __name__ == "__main__":
    start()
