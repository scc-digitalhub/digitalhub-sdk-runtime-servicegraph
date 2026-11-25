# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import Function, SourceEntityMixin
from digitalhub.utils.file_utils import get_file_mime_type

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Status

    from digitalhub_runtime_servicegraph.entities.function.servicegraph.spec import FunctionSpecServicegraph


class FunctionServicegraph(SourceEntityMixin, Function):
    """
    FunctionServicegraph class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecServicegraph
        self.status: Status

    def _is_inlineable_source(self, path: str) -> bool:
        return path.endswith((".yaml", ".yml")) or get_file_mime_type(path) == "text/yaml"
