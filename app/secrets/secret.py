# secret.py
"""Loads secrets.json and returns it as dictionary"""

import json
import os

SECRETS_PATH = os.path.join(os.path.dirname(__file__), 'secrets.json')


def get_secret():
    secrets = json.loads(open(SECRETS_PATH, 'r').read())

    if not secrets['OCR_API_KEY']:
        raise ValueError('OCR_API_KEY is not detected in secrets.json file')
    if not secrets['WOLFRAMALPHA_APP_ID']:
        raise ValueError(
            'WOLFRAMALPHA_APP_ID is not detected in secrets.json file')

    return secrets
