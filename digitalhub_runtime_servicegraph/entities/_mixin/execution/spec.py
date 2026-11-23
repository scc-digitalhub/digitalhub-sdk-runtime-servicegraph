# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._mixin.execution.spec import ServeSpecMixin
from pydantic import Field


class ServicegraphServeSpecMixin(ServeSpecMixin):
    """Serve fields shared by ServiceGraph tasks and runs."""

    replicas: int | None = Field(default=None, ge=1)
