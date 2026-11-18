# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities._mixin.source.builder import SourceBuilderMixin
from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_servicegraph.entities._base.runtime_entity.builder import RuntimeEntityBuilderServicegraph
from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds
from digitalhub_runtime_servicegraph.entities.function.servicegraph.entity import FunctionServicegraph
from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph


class FunctionServicegraphBuilder(SourceBuilderMixin, FunctionBuilder, RuntimeEntityBuilderServicegraph):
    """
    FunctionServicegraph builder.
    """

    ENTITY_CLASS = FunctionServicegraph
    ENTITY_SPEC_CLASS = FunctionSpecServicegraph
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_SERVICEGRAPH.value
