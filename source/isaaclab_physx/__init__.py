"""Compatibility shim for environments expecting ``isaaclab_physx``.

This project vendors a reduced Isaac Lab snapshot that does not ship the legacy
``isaaclab_physx`` package. The shim provides enough API surface for
``IsaacLab-Arena`` replay/runtime paths that import ``PhysxCfg`` and
renderer helpers.
"""

from .physics import PhysxCfg
