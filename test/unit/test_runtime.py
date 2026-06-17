# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest

from digitalhub_runtime_servicegraph.runtimes.runtime import RuntimeServicegraph


class TestRuntimeServicegraph:
    """Unit tests for RuntimeServicegraph."""

    def _make_runtime(self) -> RuntimeServicegraph:
        return RuntimeServicegraph(project="test-project")

    def _make_run(self, task_kind: str) -> dict:
        return {"spec": {"task": f"{task_kind}://projects/p/functions/servicegraph/fn:v1"}}

    def test_run_raises_not_implemented_for_serve(self):
        runtime = self._make_runtime()
        with pytest.raises(NotImplementedError, match="serve"):
            runtime.run(self._make_run("servicegraph+serve"))

    def test_run_raises_not_implemented_for_arbitrary_kind(self):
        runtime = self._make_runtime()
        with pytest.raises(NotImplementedError):
            runtime.run(self._make_run("unknown-task"))

    def test_error_message_contains_task_kind(self):
        runtime = self._make_runtime()
        task_kind = "servicegraph+serve"
        with pytest.raises(NotImplementedError) as exc_info:
            runtime.run(self._make_run(task_kind))
        assert task_kind in str(exc_info.value)
