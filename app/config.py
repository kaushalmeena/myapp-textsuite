"""Contains configurations to be used while running TextSuite."""

from os import environ
from os.path import dirname, join

from dotenv import load_dotenv


DOTENV_PATH = join(dirname(dirname(__file__)), ".env")

# Load environment variables from '.env' file
load_dotenv(dotenv_path=DOTENV_PATH)


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
