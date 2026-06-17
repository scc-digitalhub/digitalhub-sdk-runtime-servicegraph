# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from digitalhub_runtime_servicegraph.entities.run._base.spec import (
    RunSpecServicegraphRun,
    RunValidatorServicegraphRun,
)

TASK_REF = "servicegraph+serve://projects/my-project/functions/servicegraph/my-fn:v1"


class TestRunSpecServicegraphRun:
    """Unit tests for RunSpecServicegraphRun."""

    def test_task_stored(self):
        spec = RunSpecServicegraphRun(task=TASK_REF)
        assert spec.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        spec = RunSpecServicegraphRun(task=TASK_REF)
        assert spec.function is None
        assert spec.source is None
        assert spec.image is None
        assert spec.service_type is None
        assert spec.service_name is None
        assert spec.replicas is None
        assert spec.parameters is None

    def test_source_set(self):
        src = {"source": "src/handler.yaml"}
        spec = RunSpecServicegraphRun(task=TASK_REF, source=src)
        assert spec.source == src

    def test_image_set(self):
        spec = RunSpecServicegraphRun(task=TASK_REF, image="myimage:1.0")
        assert spec.image == "myimage:1.0"

    def test_replicas_set(self):
        spec = RunSpecServicegraphRun(task=TASK_REF, replicas=5)
        assert spec.replicas == 5

    def test_parameters_set(self):
        params = {"threshold": 0.5, "batch_size": 32}
        spec = RunSpecServicegraphRun(task=TASK_REF, parameters=params)
        assert spec.parameters == params

class TestRunValidatorServicegraphRun:
    """Unit tests for RunValidatorServicegraphRun Pydantic validator."""

    def test_valid_minimal(self):
        v = RunValidatorServicegraphRun(task=TASK_REF)
        assert v.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        v = RunValidatorServicegraphRun(task=TASK_REF)
        assert v.source is None
        assert v.image is None
        assert v.service_type is None
        assert v.service_name is None
        assert v.replicas is None
        assert v.parameters is None

    def test_image_accepted(self):
        v = RunValidatorServicegraphRun(task=TASK_REF, image="myimage:2.0")
        assert v.image == "myimage:2.0"
    def test_replicas_accepted(self):
        v = RunValidatorServicegraphRun(task=TASK_REF, replicas=3)
        assert v.replicas == 3
