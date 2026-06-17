# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_servicegraph.entities._base.runtime_entity.builder import RuntimeEntityBuilderServicegraph
from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds
from digitalhub_runtime_servicegraph.entities.task.serve.entity import TaskServicegraphServe
from digitalhub_runtime_servicegraph.entities.task.serve.spec import (
    TaskSpecServicegraphServe,
    TaskValidatorServicegraphServe,
)
from digitalhub_runtime_servicegraph.entities.task.serve.status import TaskStatusServicegraphServe


class TaskServicegraphServeBuilder(TaskBuilder, RuntimeEntityBuilderServicegraph):
    """
    TaskServicegraphServeBuilder serveer.
    """

    ENTITY_CLASS = TaskServicegraphServe
    ENTITY_SPEC_CLASS = TaskSpecServicegraphServe
    ENTITY_SPEC_VALIDATOR = TaskValidatorServicegraphServe
    ENTITY_STATUS_CLASS = TaskStatusServicegraphServe
    ENTITY_KIND = EntityKinds.TASK_SERVICEGRAPH_SERVE.value
