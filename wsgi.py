"""Contains WSGI for TextSuite."""

from os import environ

from textsuite import create_app

# Load app_config from environment variable
app_config = environ.get("APP_CONFIG", "config.DevelopmentConfig")

app = create_app(app_config)


def start():
    """Start TextSuite web server."""
    app.run()


if __name__ == "__main__":
    start()
