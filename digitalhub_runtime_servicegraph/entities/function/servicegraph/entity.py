# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities._mixin.source.entity import SourceEntityMixin
from digitalhub.entities.function._base.entity import Function
from digitalhub.utils.file_utils import get_file_mime_type

if typing.TYPE_CHECKING:
    from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph
    from digitalhub_runtime_servicegraph.entities.function.servicegraph.status import FunctionStatusServicegraph


class FunctionServicegraph(SourceEntityMixin, Function):
    """
    FunctionServicegraph class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecServicegraph
        self.status: FunctionStatusServicegraph

    def _is_inlineable_source(self, path: str) -> bool:
        return path.endswith((".yaml", ".yml")) or get_file_mime_type(path) == "text/yaml"
