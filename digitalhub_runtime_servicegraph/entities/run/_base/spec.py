# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec


class RunSpecServicegraphRun(RunSpec):
    """RunSpecServicegraphRun specifications."""

    source: dict | None = None
    image: str | None = None
    service_type: str | None = None
    service_name: str | None = None
    service_ports: list | None = None
    replicas: int | None = None
    parameters: dict | None = None


class RunValidatorServicegraphRun(RunSpecServicegraphRun):
    """Compatibility name for the typed Servicegraph run spec."""
