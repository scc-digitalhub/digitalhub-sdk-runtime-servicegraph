# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec, RunValidator


class RunSpecServicegraphRun(RunSpec):
    """RunSpecServicegraphRun specifications."""

    def __init__(
        self,
        task: str,
        function: str | None = None,
        workflow: str | None = None,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        source: dict | None = None,
        image: str | None = None,
        service_type: str | None = None,
        service_name: str | None = None,
        replicas: int | None = None,
        parameters: dict | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            task,
            function,
            workflow,
            volumes,
            resources,
            envs,
            secrets,
            profile,
            **kwargs,
        )
        self.source = source
        self.image = image
        self.service_type = service_type
        self.service_name = service_name
        self.replicas = replicas
        self.parameters = parameters


class RunValidatorServicegraphRun(RunValidator):
    """RunValidatorServicegraphRun validator."""

    # Function parameters
    source: dict | None = None
    image: str | None = None

    # Task serve
    service_type: str | None = None
    service_name: str | None = None
    replicas: int | None = None

    # Run parameters
    parameters: dict | None = None
