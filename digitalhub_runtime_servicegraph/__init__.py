# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_servicegraph.entities import entity_plugins
from digitalhub_runtime_servicegraph.entities._commons.enums import EntityKinds

entity_builders = tuple((plugin.kind, plugin.builder) for plugin in entity_plugins)

try:
    from digitalhub_runtime_servicegraph.runtimes.builder import RuntimeServicegraphBuilder

    runtime_builders = tuple((kind, RuntimeServicegraphBuilder) for kind in [e.value for e in EntityKinds])
except ImportError:
    runtime_builders = tuple()
