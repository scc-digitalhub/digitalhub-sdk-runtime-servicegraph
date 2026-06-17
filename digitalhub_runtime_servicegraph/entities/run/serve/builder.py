# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_servicegraph.entities._base.runtime_entity.builder import RuntimeEntityBuilderServicegraph
from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds
from digitalhub_runtime_servicegraph.entities.run.serve.entity import RunServicegraphRunServe
from digitalhub_runtime_servicegraph.entities.run.serve.spec import (
    RunSpecServicegraphRunServe,
    RunValidatorServicegraphRunServe,
)
from digitalhub_runtime_servicegraph.entities.run.serve.status import RunStatusServicegraphRunServe


class RunServicegraphRunServeBuilder(RunBuilder, RuntimeEntityBuilderServicegraph):
    """
    RunServicegraphRunServeBuilder runner.
    """

    ENTITY_CLASS = RunServicegraphRunServe
    ENTITY_SPEC_CLASS = RunSpecServicegraphRunServe
    ENTITY_SPEC_VALIDATOR = RunValidatorServicegraphRunServe
    ENTITY_STATUS_CLASS = RunStatusServicegraphRunServe
    ENTITY_KIND = EntityKinds.RUN_SERVICEGRAPH_SERVE.value
