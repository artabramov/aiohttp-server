"""Create config from dotenv file."""

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

    SQLALCHEMY_USERNAME: str
    SQLALCHEMY_PASSWORD: str
    SQLALCHEMY_HOST: str
    SQLALCHEMY_PORT: int
    SQLALCHEMY_DATABASE: str
    SQLALCHEMY_AUTOCOMMIT: bool
    SQLALCHEMY_AUTOFLUSH: bool


@lru_cache
def get_config() -> Config:
    """Get config object from file or cache."""
    env_values = dotenv_values(DOTENV_FILE)
    config = Config()

    for key in env_values:
        value = env_values[key]

        if value == "None":
            config.__dict__[key] = None

        elif value == "True":
            config.__dict__[key] = True

        elif value == "False":
            config.__dict__[key] = False

        elif value.isdigit():
            config.__dict__[key] = int(value)

        else:
            config.__dict__[key] = value

    return config
