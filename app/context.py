"""Context variables."""

from contextvars import ContextVar
from typing import Any

context_vars: ContextVar[dict] = ContextVar('context_vars', default={})


class LocalContext:
    """
    The class is used to declare and work with context variables.
    https://docs.python.org/3/library/contextvars.html
    """

    def __setattr__(self, key: str, value: Any) -> None:
        """Set a new value for the context variable in the current context."""
        _context_vars = context_vars.get()
        _context_vars[key] = value
        context_vars.set(_context_vars)


    def __getattr__(self, key: str):
        """Return a value for the context variable for the current context."""
        _context_vars = context_vars.get()
        return _context_vars.get(key)


ctx = LocalContext()
