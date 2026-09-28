# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder
from digitalhub_runtime_servicegraph.entities.function.servicegraph.crud import new_function_servicegraph
from digitalhub_runtime_servicegraph.entities.run.serve.builder import RunServicegraphRunServeBuilder
from digitalhub_runtime_servicegraph.entities.task.serve.builder import TaskServicegraphServeBuilder

function_servicegraph_plugin = EntityPlugin(
    builder=FunctionServicegraphBuilder,
    shortcuts=(CrudPlugin(new_function_servicegraph),),
)

entity_plugins = (
    function_servicegraph_plugin,
    EntityPlugin(builder=TaskServicegraphServeBuilder),
    EntityPlugin(builder=RunServicegraphRunServeBuilder),
)
