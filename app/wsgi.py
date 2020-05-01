"""Starts TextSuite app in production mode."""

from app.config import ProductionConfig
from app.main import app


if __name__ == "__main__":
    app.config.from_object(ProductionConfig())
    app.run()
