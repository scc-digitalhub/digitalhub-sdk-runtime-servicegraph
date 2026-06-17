# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.runtimes.builder import RuntimeBuilder

from digitalhub_runtime_servicegraph.runtimes.runtime import RuntimeServicegraph


class RuntimeServicegraphBuilder(RuntimeBuilder):
    """RuntimeServicegraphBuilder class."""

    RUNTIME_CLASS = RuntimeServicegraph
