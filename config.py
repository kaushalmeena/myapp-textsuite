"""Contains configurations to be used while running TextSuite."""

from os import environ

from dotenv import load_dotenv

# Load environment variables from '.env' file
load_dotenv()


class BaseConfig:
    """Contains base configuration to be inherited by both dev/prod configurations."""

    OCR_API_KEY = environ.get("OCR_API_KEY")
    WOLFRAMALPHA_APP_ID = environ.get("WOLFRAMALPHA_APP_ID")


class ProductionConfig(BaseConfig):
    """Contains configuration to be used while running app in production mode."""

    ENV = "production"


class DevelopmentConfig(BaseConfig):
    """Contains configuration to be used while running app in development mode."""

    ENV = "development"
    TEMPLATES_AUTO_RELOAD = True
