"""
Python script for getting API secrets.
"""

import json

from os.path import join, dirname

SECRETS_PATH = join(dirname(__file__), "secrets.json")


def get_secret():
    """
    Returns content of secrets.json as dictionary.
    """
    return json.loads(open(SECRETS_PATH, "r").read())
