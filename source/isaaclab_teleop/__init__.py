# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Package providing IsaacTeleop-based teleoperation for Isaac Lab."""

import os
import toml
ISAACLAB_TELEOP_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
"""Path to the extension source directory."""
ISAACLAB_TELEOP_METADATA = toml.load(os.path.join(ISAACLAB_TELEOP_EXT_DIR, "config", "extension.toml"))
"""Extension metadata dictionary parsed from the extension.toml file."""
__version__ = ISAACLAB_TELEOP_METADATA["package"]["version"]

try:
    from isaaclab.utils.module import lazy_export
except ImportError:  # pragma: no cover - compatibility fallback when older ISAACLAB layout is present.
    def lazy_export(*_args, **_kwargs):
        return

from .isaac_teleop_cfg import IsaacTeleopCfg
from .xr_cfg import XrAnchorRotationMode, XrCfg, remove_camera_configs


def create_isaac_teleop_device(*args, **kwargs):  # pragma: no cover
    """Lazily import heavy teleop implementation."""
    from .isaac_teleop_device import create_isaac_teleop_device as _create

    return _create(*args, **kwargs)

__all__ = [
    "IsaacTeleopCfg",
    "XrCfg",
    "XrAnchorRotationMode",
    "create_isaac_teleop_device",
    "remove_camera_configs",
]

lazy_export()
