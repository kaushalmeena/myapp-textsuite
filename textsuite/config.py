# config.py
"""Python script for TextSuite configuration."""

from dotenv import load_dotenv
from os import environ

load_dotenv(verbose=True)


class Config():
    OCR_API_KEY = environ.get('OCR_API_KEY')
    WOLFRAMALPHA_APP_ID = environ.get('WOLFRAMALPHA_APP_ID')


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
