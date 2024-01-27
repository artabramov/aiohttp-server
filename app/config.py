"""Create config from dotenv file."""

import os
from dotenv import dotenv_values
from functools import lru_cache

DOTENV_FILE = "/hide/.env"


class Config:
    """Config dataclass."""

    LOG_LEVEL: str
    LOG_FORMAT: str
    LOG_FILENAME: str
    LOG_FILESIZE: int
    LOG_FILES_LIMIT: int


def set_config(app):
    """Set config for aiohttp app."""
    config = dotenv_values(DOTENV_FILE)
    for key in config:
        value = config[key]
        if value == "None":
            value = None

        elif value == "True":
            value = True

        elif value == "False":
            value = False

        elif value.isdigit():
            value = int(value)

        app[key] = value
    return config
