# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Spec

from digitalhub_runtime_servicegraph.entities.function.servicegraph.models import ServicegraphSourceCode


class FunctionSpecServicegraph(Spec):
    """
    FunctionSpecServicegraph specifications.
    """

    source: ServicegraphSourceCode | None = None
    image: str | None = None
