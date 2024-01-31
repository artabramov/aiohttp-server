"""Create config."""

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

    PG_USERNAME: str
    PG_PASSWORD: str
    PG_HOST: str
    PG_PORT: int
    PG_DATABASE: str
    PG_AUTOCOMMIT: bool
    PG_AUTOFLUSH: bool


@lru_cache
def get_config() -> Config:
    """Create config object from dotenv file."""
    env_values = dotenv_values(DOTENV_FILE)
    config = Config()

    for key in env_values:
        value = env_values[key]

        if Config.__annotations__[key] == str:
            config.__dict__[key] = value

        elif Config.__annotations__[key] == int:
            config.__dict__[key] = int(value)

        elif Config.__annotations__[key] == bool:
            config.__dict__[key] = True if value.lower() == "true" else False

        else:
            config.__dict__[key] = None

    return config
