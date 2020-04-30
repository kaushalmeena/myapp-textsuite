"""
Python script for TextSuite configuration.
"""

from app.secrets.secret import get_secret

# Load secrets from secrets.json file
SECRETS = get_secret()


class BaseConfig:
    OCR_API_KEY = SECRETS["OCR_API_KEY"]
    WOLFRAMALPHA_APP_ID = SECRETS["WOLFRAMALPHA_APP_ID"]


class ProductionConfig(BaseConfig):
    ENV = "production"


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    TEMPLATES_AUTO_RELOAD = True
