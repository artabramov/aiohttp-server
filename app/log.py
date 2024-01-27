"""Provides Postgres database session object."""
import logging
from logging.handlers import RotatingFileHandler
from logging import Filter
from uuid import uuid4


def get_log(request):
    """Get logger object."""
    class ContextualFilter(Filter):
        """Contextual filter for logging."""
        request["trace_request_uuid"] = str(uuid4())

        def filter(self, message: object) -> bool:
            """Customize the contextual filter."""
            message.uuid = request["trace_request_uuid"]
            return True


    handler = RotatingFileHandler(filename=request.app["LOG_FILENAME"], maxBytes=request.app["LOG_FILESIZE"], backupCount=request.app["LOG_FILES_LIMIT"])
    handler.setFormatter(logging.Formatter(request.app["LOG_FORMAT"]))

    log = logging.getLogger(__name__)
    log.addHandler(handler)
    log.addFilter(ContextualFilter())
    log.setLevel(logging.getLevelName(request.app["LOG_LEVEL"]))

    return log
