"""Compatibility helpers used by ``isaaclab_arena`` runtime patching."""

_last_render_update_key = (None, -1)
_streaming_is_busy = False
_streaming_subscribed = False
_streaming_subscription = None


def ensure_isaac_rtx_render_update() -> None:
    """No-op shim for environments without the original PhysX renderer helpers."""
    return None


def _ensure_streaming_subscription() -> None:
    global _streaming_subscribed
    _streaming_subscribed = True


def _wait_for_streaming_complete() -> None:
    return None
