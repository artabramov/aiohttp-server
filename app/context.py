"""Context variables."""

from contextvars import ContextVar
from typing import Any

context_vars: ContextVar[dict] = ContextVar('context_vars', default={})


def set_ctx_var(key: str, value: Any) -> None:
    """Set a new value for the context variable in the current context."""
    _context_data = context_vars.get()
    _context_data[key] = value
    context_vars.set(_context_data)


def get_ctx_var(key: str):
    """Return a value for the context variable for the current context."""
    _context_data = context_vars.get()
    return _context_data.get(key)
