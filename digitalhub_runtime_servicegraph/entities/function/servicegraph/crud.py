# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_servicegraph.entities.function.servicegraph.builder import FunctionServicegraphBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_servicegraph.entities.function.servicegraph.entity import FunctionServicegraph


def new_function_servicegraph(
    project: str,
    name: str,
    image: str | None = None,
    source: dict | None = None,
    code: str | None = None,
    code_src: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionServicegraph:
    """Create a servicegraph function entity."""
    if code is not None and code_src is not None:
        raise ValueError("Only one of 'code' or 'code_src' can be provided.")

    return new_function(
        project=project,
        name=name,
        kind=FunctionServicegraphBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        image=image,
        source=source,
        code=code,
        code_src=code_src,
    )
