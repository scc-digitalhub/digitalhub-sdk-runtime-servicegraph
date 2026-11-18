# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import ServeSpecMixin, TaskSpecFunction
from pydantic import Field


class ServicegraphServeSpecMixin(ServeSpecMixin):
    """Servicegraph-specific compatibility layer for serve fields."""

    replicas: int | None = Field(default=None, ge=1)


class TaskSpecServicegraphServe(TaskSpecFunction, ServicegraphServeSpecMixin):
    """TaskSpecServicegraphServe specifications."""


TaskValidatorServicegraphServe = TaskSpecServicegraphServe
