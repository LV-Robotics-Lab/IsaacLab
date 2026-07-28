"""Minimal ``isaaclab_physx`` physics compatibility API."""

from __future__ import annotations

from typing import Any


class PhysxCfg:
    """Lightweight replacement for the Isaac Lab PhysX configuration class."""

    def __init__(self, **kwargs: Any) -> None:
        # Use the common PhysX fields as defaults; callers can overwrite anything.
        self.enable_scene_query_support: bool = kwargs.pop("enable_scene_query_support", True)
        self.solver_type: int = kwargs.pop("solver_type", 1)
        self.gpu_max_rigid_contact_count: int = kwargs.pop("gpu_max_rigid_contact_count", 262_144)
        self.gpu_found_lost_pairs_capacity: int = kwargs.pop("gpu_found_lost_pairs_capacity", 262_144)
        self.gpu_found_lost_aggregate_pairs_capacity: int = kwargs.pop(
            "gpu_found_lost_aggregate_pairs_capacity",
            262_144,
        )
        self.gpu_total_aggregate_pairs_capacity: int = kwargs.pop(
            "gpu_total_aggregate_pairs_capacity",
            4 * 1024 * 1024,
        )
        self.gpu_collision_stack_size: int = kwargs.pop("gpu_collision_stack_size", 1_024_000)
        self.gpu_temp_buffer_capacity: int = kwargs.pop("gpu_temp_buffer_capacity", 24 * 1024 * 1024)
        self.gpu_max_rigid_patch_count: int = kwargs.pop("gpu_max_rigid_patch_count", 8_192)
        self.gpu_heap_capacity: int = kwargs.pop("gpu_heap_capacity", 64 * 1024 * 1024)
        self.simulation_offset = kwargs.pop("simulation_offset", (0.0, 0.0, 0.0))
        self.enable_stablization = kwargs.pop("enable_stablization", False)
        self.friction_offset_threshold = kwargs.pop("friction_offset_threshold", 0.04)
        self.rest_offset = kwargs.pop("rest_offset", 0.0)
        # Store any extra values to emulate flexible config objects.
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self) -> str:  # pragma: no cover - diagnostic helper
        return "PhysxCfg()"
