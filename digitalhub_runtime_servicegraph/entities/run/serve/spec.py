# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_servicegraph.entities._mixin.execution.spec import ServicegraphServeSpecMixin
from digitalhub_runtime_servicegraph.entities.run._base.spec import RunSpecServicegraphRun


class RunSpecServicegraphRunServe(RunSpecServicegraphRun, ServicegraphServeSpecMixin):
    """RunSpecServicegraphRunServe specifications."""
