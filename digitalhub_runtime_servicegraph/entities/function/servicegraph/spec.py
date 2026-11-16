# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec

from digitalhub_runtime_servicegraph.entities.function.servicegraph.models import ServicegraphSourceCode


class FunctionSpecServicegraph(FunctionSpec):
    """
    FunctionSpecServicegraph specifications.
    """

    source: ServicegraphSourceCode | None = None
    image: str | None = None


class FunctionValidatorServicegraph(FunctionSpecServicegraph):
    """Compatibility name for the typed Servicegraph function spec."""
