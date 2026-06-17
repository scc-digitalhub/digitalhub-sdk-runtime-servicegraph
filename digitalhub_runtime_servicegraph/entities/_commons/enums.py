# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_SERVICEGRAPH = "servicegraph"
    TASK_SERVICEGRAPH_SERVE = "servicegraph+serve"
    RUN_SERVICEGRAPH_SERVE = "servicegraph+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    SERVE = "serve"
