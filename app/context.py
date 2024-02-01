"""Context-local variables storage."""

from contextvars import ContextVar
from typing import Any

ctx_vars: ContextVar[dict] = ContextVar('ctx_vars', default={})


class LocalContext:
    """
    The class is used to declare and work with context variables
    (a thread-local concept that works with asyncio tasks also).
    https://docs.python.org/3/library/contextvars.html
    """

    def __setattr__(self, key: str, value: Any) -> None:
        """Set a new value for the context variable in the current context."""
        vars = ctx_vars.get()
        vars[key] = value
        ctx_vars.set(vars)


    def __getattr__(self, key: str):
        """Return a value for the context variable for the current context."""
        vars = ctx_vars.get()
        return vars.get(key)


ctx = LocalContext()
