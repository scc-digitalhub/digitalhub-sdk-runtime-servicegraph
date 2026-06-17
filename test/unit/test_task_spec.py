# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pytest
from pydantic import ValidationError

from digitalhub_runtime_servicegraph.entities.task.serve.spec import (
    TaskSpecServicegraphServe,
    TaskValidatorServicegraphServe,
)

FUNCTION_REF = "store://projects/my-project/functions/servicegraph/my-fn:v1"

class TestTaskSpecServicegraphServe:
    """Unit tests for TaskSpecServicegraphServe."""

    def test_function_ref_stored(self):
        spec = TaskSpecServicegraphServe(function=FUNCTION_REF)
        assert spec.function == FUNCTION_REF

    def test_optional_fields_default_to_none(self):
        spec = TaskSpecServicegraphServe(function=FUNCTION_REF)
        assert spec.replicas is None
        assert spec.service_type is None
        assert spec.service_name is None

    def test_replicas_set(self):
        spec = TaskSpecServicegraphServe(function=FUNCTION_REF, replicas=3)
        assert spec.replicas == 3

    def test_service_type_set(self):
        spec = TaskSpecServicegraphServe(function=FUNCTION_REF, service_type="NodePort")
        assert spec.service_type == "NodePort"

    def test_service_name_set(self):
        spec = TaskSpecServicegraphServe(function=FUNCTION_REF, service_name="my-svc")
        assert spec.service_name == "my-svc"


class TestTaskValidatorServicegraphServe:
    """Unit tests for TaskValidatorServicegraphServe Pydantic validator."""

    def test_valid_minimal(self):
        v = TaskValidatorServicegraphServe(function=FUNCTION_REF)
        assert v.function == FUNCTION_REF
        assert v.replicas is None
        assert v.service_type is None
        assert v.service_name is None

    def test_replicas_accepted(self):
        v = TaskValidatorServicegraphServe(function=FUNCTION_REF, replicas=2)
        assert v.replicas == 2

    def test_replicas_must_be_at_least_one(self):
        with pytest.raises(ValidationError):
            TaskValidatorServicegraphServe(function=FUNCTION_REF, replicas=0)

    def test_negative_replicas_raises(self):
        with pytest.raises(ValidationError):
            TaskValidatorServicegraphServe(function=FUNCTION_REF, replicas=-1)

    def test_service_name_accepted(self):
        v = TaskValidatorServicegraphServe(function=FUNCTION_REF, service_name="inference-svc")
        assert v.service_name == "inference-svc"
