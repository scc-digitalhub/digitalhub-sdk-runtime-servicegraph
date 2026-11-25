# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest
from digitalhub.plugins import build_spec

from digitalhub_runtime_servicegraph.entities._mixin.execution.spec import ServicegraphServeSpecMixin
from digitalhub_runtime_servicegraph.entities.run._base.spec import (
    RunSpecServicegraphRun,
)
from digitalhub_runtime_servicegraph.entities.run.serve.spec import (
    RunSpecServicegraphRunServe,
)
from digitalhub_runtime_servicegraph.entities.task.serve.spec import TaskSpecServicegraphServe

TASK_REF = "servicegraph+serve://projects/my-project/functions/servicegraph/my-fn:v1"
FUNCTION_REF = "servicegraph://projects/my-project/functions/servicegraph/my-fn:v1"


def test_serve_spec_mixin_has_one_runtime_owner():
    assert ServicegraphServeSpecMixin in TaskSpecServicegraphServe.__mro__
    assert ServicegraphServeSpecMixin in RunSpecServicegraphRunServe.__mro__


class TestRunSpecServicegraphRun:
    """Unit tests for RunSpecServicegraphRun."""

    def test_task_stored(self):
        spec = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF)
        assert spec.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        spec = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF)
        assert spec.function == FUNCTION_REF
        assert spec.source is None
        assert spec.image is None
        assert spec.parameters is None

    def test_source_set(self):
        src = {"source": "src/handler.yaml"}
        spec = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF, source=src)
        assert spec.source == src

    def test_image_set(self):
        spec = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF, image="myimage:1.0")
        assert spec.image == "myimage:1.0"

    def test_replicas_set(self):
        spec = RunSpecServicegraphRunServe(function=FUNCTION_REF, task=TASK_REF, replicas=5)
        assert spec.replicas == 5

    def test_parameters_set(self):
        params = {"threshold": 0.5, "batch_size": 32}
        spec = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF, parameters=params)
        assert spec.parameters == params


class TestRunSpecServicegraphRunValidation:
    """Unit tests for Servicegraph run-spec validation."""

    def test_valid_minimal(self):
        v = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF)
        assert v.task == TASK_REF

    def test_optional_fields_default_to_none(self):
        v = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF)
        assert v.source is None
        assert v.image is None
        assert v.parameters is None

    def test_image_accepted(self):
        v = RunSpecServicegraphRun(function=FUNCTION_REF, task=TASK_REF, image="myimage:2.0")
        assert v.image == "myimage:2.0"

    def test_replicas_accepted(self):
        v = RunSpecServicegraphRunServe(function=FUNCTION_REF, task=TASK_REF, replicas=3)
        assert v.replicas == 3

    def test_serve_fields_are_scoped_to_serve_run(self):
        run = build_spec(
            RunSpecServicegraphRunServe,
            function=FUNCTION_REF,
            task=TASK_REF,
            replicas=2,
            service_type="ClusterIP",
        )
        assert run.replicas == 2
        assert run.service_type == "ClusterIP"

        with pytest.raises(TypeError, match="service_type"):
            build_spec(
                RunSpecServicegraphRun,
                function=FUNCTION_REF,
                task=TASK_REF,
                service_type="ClusterIP",
            )

    def test_run_parameters_do_not_leak_into_task_specs(self):
        run = build_spec(
            RunSpecServicegraphRun,
            function=FUNCTION_REF,
            task=TASK_REF,
            parameters={"limit": 10},
        )
        assert run.parameters == {"limit": 10}

        with pytest.raises(TypeError, match="parameters"):
            build_spec(TaskSpecServicegraphServe, function=TASK_REF, parameters={"limit": 10})
