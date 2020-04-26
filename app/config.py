# config.py
"""Python script for TextSuite configuration."""

from dotenv import load_dotenv
from os import getenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path=dotenv_path, verbose=True)


class Config():
    OCR_API_KEY = getenv('OCR_API_KEY')
    WOLFRAMALPHA_APP_ID = getenv('WOLFRAMALPHA_APP_ID')


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
