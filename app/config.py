# config.py
"""Python script for TextSuite configuration."""

from dotenv import load_dotenv

import os

DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')

# Load environment variables from '.env' file
load_dotenv(dotenv_path=DOTENV_PATH, verbose=True)


class Config():
    OCR_API_KEY = os.getenv('OCR_API_KEY')
    WOLFRAMALPHA_APP_ID = os.getenv('WOLFRAMALPHA_APP_ID')

    def __init__(self):
        if not self.OCR_API_KEY:
            raise ValueError(
                'OCR_API_KEY is not detected in .env file')
        if not self.WOLFRAMALPHA_APP_ID:
            raise ValueError(
                'WOLFRAMALPHA_APP_ID is not detected in .env file')


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
