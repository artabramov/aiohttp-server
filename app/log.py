"""Provides Postgres database session object."""
import logging
from logging.handlers import RotatingFileHandler
from logging import Filter
from appconfig import  get_config
from context import ctx


config = get_config()


class ContextualFilter(Filter):
    """Contextual filter for logging."""

    def filter(self, message: object) -> bool:
        """Customize the contextual filter."""
        message.trace_request_uuid = ctx.trace_request_uuid
        message.pid = ctx.pid
        return True


handler = RotatingFileHandler(filename=config.LOG_FILENAME, maxBytes=config.LOG_FILESIZE, backupCount=config.LOG_FILES_LIMIT)
handler.setFormatter(logging.Formatter(config.LOG_FORMAT))

log = logging.getLogger(__name__)
log.addHandler(handler)
log.addFilter(ContextualFilter())
log.setLevel(logging.getLevelName(config.LOG_LEVEL))
