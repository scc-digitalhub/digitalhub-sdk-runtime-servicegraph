# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_SERVICEGRAPH = "openinference"
    TASK_SERVICEGRAPH_SERVE = "openinference+serve"
    RUN_SERVICEGRAPH_SERVE = "openinference+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    SERVE = "serve"
