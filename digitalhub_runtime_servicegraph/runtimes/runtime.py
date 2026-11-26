# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import EntityRef, Runtime


class RuntimeServicegraph(Runtime):
    """
    Runtime Servicegraph class.
    """

    def run(self, run: dict) -> dict:
        """
        Run function.

        Returns
        -------
        dict
            Status of the executed run.
        """
        task_kind = EntityRef.parse(run["spec"]["task"]).kind
        raise NotImplementedError(f"Local execution not implemented for task kind: {task_kind}")
