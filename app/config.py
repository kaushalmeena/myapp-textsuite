"""
Python script for TextSuite configuration.
"""

from dotenv import load_dotenv

from os import environ
from os.path import join, dirname

DOTENV_PATH = join(dirname(dirname(__file__)), ".env")

# Load environment variables from '.env' file
load_dotenv(dotenv_path=DOTENV_PATH)


class BaseConfig:
    OCR_API_KEY = environ.get("OCR_API_KEY")
    WOLFRAMALPHA_APP_ID = environ.get("WOLFRAMALPHA_APP_ID")


class ProductionConfig(BaseConfig):
    ENV = "production"


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    TEMPLATES_AUTO_RELOAD = True
