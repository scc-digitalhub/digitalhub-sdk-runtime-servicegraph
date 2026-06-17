# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds
from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder
from digitalhub_runtime_servicegraph.entities.run.serve.builder import RunServicegraphRunServeBuilder
from digitalhub_runtime_servicegraph.entities.task.serve.builder import TaskServicegraphServeBuilder

entity_builders = (
    (EntityKinds.FUNCTION_SERVICEGRAPH.value, FunctionServicegraphBuilder),
    (EntityKinds.TASK_SERVICEGRAPH_SERVE.value, TaskServicegraphServeBuilder),
    (EntityKinds.RUN_SERVICEGRAPH_SERVE.value, RunServicegraphRunServeBuilder),
)

try:
    from digitalhub_runtime_servicegraph.runtimes.builder import RuntimeServicegraphBuilder

    runtime_builders = ((kind, RuntimeServicegraphBuilder) for kind in [e.value for e in EntityKinds])
except ImportError:
    runtime_builders = tuple()
