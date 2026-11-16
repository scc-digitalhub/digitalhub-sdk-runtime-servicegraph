# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder
from digitalhub_runtime_servicegraph.entities.function.servicegraph.entity import FunctionServicegraph
from digitalhub_runtime_servicegraph.entities.function.servicegraph.models import SourceValidator
from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph


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

    def test_post_build_source_check_uses_nested_source_model(self):
        executable = object.__new__(FunctionServicegraph)
        executable.spec = FunctionSpecServicegraph(source={"source": "s3://bucket/source.yaml"})

        assert executable._post_build_source_check() is executable

    def test_builder_routes_top_level_source_code(self):
        builder = FunctionServicegraphBuilder()

        function = builder.build(
            kind=builder.ENTITY_KIND,
            project="project",
            name="function",
            code="services: {}",
        )

        assert function.spec.source.base64 == "c2VydmljZXM6IHt9"
        assert function.spec.source.lang == "yaml"
