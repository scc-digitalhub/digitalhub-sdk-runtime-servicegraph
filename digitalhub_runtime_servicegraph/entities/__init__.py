# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    ExecutableActions,
    FunctionBuilder,
    RunBuilder,
    SourceBuilderMixin,
    Status,
    Task,
    TaskBuilder,
)

from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds
from digitalhub_runtime_servicegraph.entities.function.servicegraph.crud import new_function_servicegraph
from digitalhub_runtime_servicegraph.entities.function.servicegraph.entity import FunctionServicegraph
from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph
from digitalhub_runtime_servicegraph.entities.run._base.entity import RunServicegraphRun
from digitalhub_runtime_servicegraph.entities.run._base.status import RunStatusServicegraphRun
from digitalhub_runtime_servicegraph.entities.run.serve.spec import RunSpecServicegraphRunServe
from digitalhub_runtime_servicegraph.entities.task.serve.spec import TaskSpecServicegraphServe

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_SERVICEGRAPH_BUILDER = "digitalhub_runtime_servicegraph.runtimes.builder:RuntimeServicegraphBuilder"

servicegraph = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_SERVICEGRAPH,
        FunctionServicegraph,
        FunctionSpecServicegraph,
        Status,
        base=FunctionBuilder,
        mixins=(SourceBuilderMixin,),
        shortcuts=(CrudPlugin(new_function_servicegraph),),
    ),
    actions={
        ExecutableActions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_SERVICEGRAPH_SERVE,
                Task,
                TaskSpecServicegraphServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_SERVICEGRAPH_SERVE,
                RunServicegraphRun,
                RunSpecServicegraphRunServe,
                RunStatusServicegraphRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_SERVICEGRAPH_BUILDER,
)

entity_plugins = (*servicegraph.plugins(),)
