# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder
from digitalhub_runtime_servicegraph.entities.function.servicegraph.crud import new_function_servicegraph
from digitalhub_runtime_servicegraph.entities.run.serve.builder import RunServicegraphRunServeBuilder
from digitalhub_runtime_servicegraph.entities.task.serve.builder import TaskServicegraphServeBuilder

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_SERVICEGRAPH_BUILDER = "digitalhub_runtime_servicegraph.runtimes.builder:RuntimeServicegraphBuilder"

function_servicegraph_plugin = EntityPlugin(
    builder=FunctionServicegraphBuilder,
    shortcuts=(CrudPlugin(new_function_servicegraph),),
    runtime_builder=RUNTIME_SERVICEGRAPH_BUILDER,
)

entity_plugins = (
    function_servicegraph_plugin,
    EntityPlugin(builder=TaskServicegraphServeBuilder, runtime_builder=RUNTIME_SERVICEGRAPH_BUILDER),
    EntityPlugin(builder=RunServicegraphRunServeBuilder, runtime_builder=RUNTIME_SERVICEGRAPH_BUILDER),
)
