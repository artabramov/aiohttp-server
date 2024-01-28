"""Provides Postgres database session object."""
import logging
from logging.handlers import RotatingFileHandler
from logging import Filter
from config import  get_config
from context import ctx


config = get_config()


class ContextualFilter(Filter):
    """Contextual filter for logging."""
    def filter(self, message: object) -> bool:
        """Customize the contextual filter."""
        message.trace_request_uuid = ctx.trace_request_uuid
        message.pid = ctx.pid
        tmp = ctx.request_start_time
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
