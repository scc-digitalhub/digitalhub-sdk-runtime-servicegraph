# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import (
    FunctionSpecServicegraph,
    FunctionValidatorServicegraph,
)


class TestFunctionSpecServicegraph:
    """Unit tests for FunctionSpecServicegraph constructor and attributes."""

    def test_defaults_to_none(self):
        spec = FunctionSpecServicegraph()
        assert spec.image is None
        assert spec.source is None

    def test_image_set(self):
        spec = FunctionSpecServicegraph(image="my-registry/my-image:latest")
        assert spec.image == "my-registry/my-image:latest"

    def test_source_set(self):
        src = {"source": "src/handler.yaml"}
        spec = FunctionSpecServicegraph(source=src)
        assert spec.source == src

    def test_all_params(self):
        spec = FunctionSpecServicegraph(
            source={"source": "src/main.yaml"},
            image="myimage:1.0",
        )
        assert spec.image == "myimage:1.0"
        assert spec.source == {"source": "src/main.yaml"}


class TestFunctionValidatorServicegraph:
    """Unit tests for FunctionValidatorServicegraph Pydantic validator."""

    _BASE_VALID = {
        "source": {"source": "src/handler.yaml"},
    }

    def test_optional_fields_default_to_none(self):
        validator = FunctionValidatorServicegraph(**self._BASE_VALID)
        assert validator.image is None

    def test_with_image(self):
        data = {**self._BASE_VALID, "image": "myimage:latest"}
        validator = FunctionValidatorServicegraph(**data)
        assert validator.image == "myimage:latest"