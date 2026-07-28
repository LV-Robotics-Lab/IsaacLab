"""Compatibility helpers for IsaacLab utility exports.

Some downstream packages import :func:`lazy_export` from this module. The function is
implemented as a no-op because the lightweight local environment does not require
lazy symbol re-export behavior.
"""


def lazy_export(*_args, **_kwargs):  # pragma: no cover - compatibility shim
    return
