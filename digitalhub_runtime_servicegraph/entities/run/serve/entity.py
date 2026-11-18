# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_servicegraph.entities.run._base.entity import RunServicegraphRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_servicegraph.entities.run._base.status import RunStatusServicegraphRun
    from digitalhub_runtime_servicegraph.entities.run.serve.spec import RunSpecServicegraphRunServe


class RunServicegraphRunServe(RunServicegraphRun):
    """
    RunServicegraphRunServe class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecServicegraphRunServe
        self.status: RunStatusServicegraphRun
