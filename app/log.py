"""Provides Postgres database session object."""
import logging
from logging.handlers import RotatingFileHandler
from logging import Filter
from context import get_ctx_var
from config import  get_config


config = get_config()


class ContextualFilter(Filter):
    """Contextual filter for logging."""
    def filter(self, message: object) -> bool:
        """Customize the contextual filter."""
        message.trace_request_uuid = get_ctx_var("trace_request_uuid")
        message.pid = get_ctx_var("pid")
        return True


def get_log():
    """Get logger object."""
    handler = RotatingFileHandler(filename=config.LOG_FILENAME, maxBytes=config.LOG_FILESIZE, backupCount=config.LOG_FILES_LIMIT)
    handler.setFormatter(logging.Formatter(config.LOG_FORMAT))

    log = logging.getLogger(__name__)
    log.addHandler(handler)
    log.addFilter(ContextualFilter())
    log.setLevel(logging.getLevelName(config.LOG_LEVEL))

    return log
