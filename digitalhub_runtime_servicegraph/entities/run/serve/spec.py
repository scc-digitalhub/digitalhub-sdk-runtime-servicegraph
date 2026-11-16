# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_servicegraph.entities.run._base.spec import RunSpecServicegraphRun
from digitalhub_runtime_servicegraph.entities.task.serve.spec import ServicegraphServeSpecMixin


class RunSpecServicegraphRunServe(RunSpecServicegraphRun, ServicegraphServeSpecMixin):
    """RunSpecServicegraphRunServe specifications."""


class RunValidatorServicegraphRunServe(RunSpecServicegraphRunServe):
    """Compatibility name for the typed Servicegraph serve-run spec."""
