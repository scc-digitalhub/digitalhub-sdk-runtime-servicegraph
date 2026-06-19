# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.models import CoreServiceType
from digitalhub.entities.task._base.spec import TaskSpecFunction, TaskValidatorFunction
from pydantic import Field


class TaskSpecServicegraphServe(TaskSpecFunction):
    """TaskSpecServicegraphServe specifications."""

    def __init__(
        self,
        function: str,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        replicas: int | None = None,
        service_type: str | None = None,
        service_name: str | None = None,
        service_ports: list | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            function,
            volumes,
            resources,
            envs,
            secrets,
            profile,
            **kwargs,
        )
        self.replicas = replicas
        self.service_type = service_type
        self.service_name = service_name
        self.service_ports = service_ports

class TaskValidatorServicegraphServe(TaskValidatorFunction):
    """
    TaskValidatorServicegraphServe validator.
    """

    replicas: int | None = Field(default=None, ge=1)
    """Number of replicas."""

    service_type: CoreServiceType | None = None
    """Service type."""

    service_name: str | None = None
    """Service name."""

    service_ports: list | None = None
    """Service ports."""
