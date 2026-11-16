# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from types import SimpleNamespace

from digitalhub_runtime_servicegraph.entities.function.servicegraph.models import SourceValidator
from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph
from digitalhub_runtime_servicegraph.entities.function.servicegraph.utlis import source_post_check


class TestFunctionSpecServicegraph:
    """Unit tests for the typed FunctionSpecServicegraph model."""

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
        assert isinstance(spec.source, SourceValidator)
        assert spec.source.source == src["source"]

    def test_all_params(self):
        spec = FunctionSpecServicegraph(
            source={"source": "src/main.yaml"},
            image="myimage:1.0",
        )
        assert spec.image == "myimage:1.0"
        assert spec.source.source == "src/main.yaml"
        assert spec.to_dict() == {
            "image": "myimage:1.0",
            "source": {"lang": "yaml", "source": "src/main.yaml"},
        }

    def test_source_post_check_uses_nested_source_model(self):
        executable = SimpleNamespace(spec=FunctionSpecServicegraph(source={"source": "s3://bucket/source.yaml"}))

        assert source_post_check(executable) is executable
