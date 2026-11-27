# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import Run, ServeRunMixin

if typing.TYPE_CHECKING:
    from digitalhub_runtime_servicegraph.entities.run._base.spec import RunSpecServicegraphRun
    from digitalhub_runtime_servicegraph.entities.run._base.status import RunStatusServicegraphRun


class RunServicegraphRun(ServeRunMixin, Run):
    """
    RunServicegraphRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecServicegraphRun
        self.status: RunStatusServicegraphRun

    def _setup_execution(self) -> None:
        """
        Setup run execution.
        """
        self.refresh()
