# config.py
"""Python script for TextSuite configuration."""

from app.secrets.secret import get_secret
import os

# Load secrets from secrets.json file
SECRETS = get_secret()


class Config():
    OCR_API_KEY = SECRETS['OCR_API_KEY']
    WOLFRAMALPHA_APP_ID = SECRETS['WOLFRAMALPHA_APP_ID']


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
