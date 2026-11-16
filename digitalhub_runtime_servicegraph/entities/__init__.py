# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder
from digitalhub_runtime_servicegraph.entities.function.servicegraph.crud import new_function_servicegraph
from digitalhub_runtime_servicegraph.entities.run.serve.builder import RunServicegraphRunServeBuilder
from digitalhub_runtime_servicegraph.entities.task.serve.builder import TaskServicegraphServeBuilder

try:
    from digitalhub_runtime_servicegraph.runtimes.builder import RuntimeServicegraphBuilder
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    get_logger(__name__).debug(f"Error importing runtime builder: {e}")
    RuntimeServicegraphBuilder = None

function_servicegraph_plugin = EntityPlugin(
    builder=FunctionServicegraphBuilder,
    shortcuts=(CrudPlugin(new_function_servicegraph),),
    runtime_builder=RuntimeServicegraphBuilder,
)

entity_plugins = (
    function_servicegraph_plugin,
    EntityPlugin(builder=TaskServicegraphServeBuilder, runtime_builder=RuntimeServicegraphBuilder),
    EntityPlugin(builder=RunServicegraphRunServeBuilder, runtime_builder=RuntimeServicegraphBuilder),
)
