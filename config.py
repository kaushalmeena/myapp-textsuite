"""Contains configurations to be used while running textsuite app."""

from os import environ

from dotenv import load_dotenv

# Load environment variables from '.env' file
load_dotenv()


class BaseConfig:
    """Contains base configuration to be inherited by both dev/prod configurations."""

    OCR_API_KEY = environ.get("OCR_API_KEY")
    OCR_API_URL = "https://api.ocr.space/parse/image"
    WOLFRAMALPHA_APP_ID = environ.get("WOLFRAMALPHA_APP_ID")
    WOLFRAMALPHA_API_URL = "http://api.wolframalpha.com/v1/simple"


class ProductionConfig(BaseConfig):
    """Contains configuration to be used while running app in production mode."""

    ENV = "production"


class DevelopmentConfig(BaseConfig):
    """Contains configuration to be used while running app in development mode."""

    ENV = "development"
    DEBUG = True
