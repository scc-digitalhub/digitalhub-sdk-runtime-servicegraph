# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator
from digitalhub_runtime_python.entities.function.python.models import SourceValidator


class FunctionSpecServicegraph(FunctionSpec):
    """
    FunctionSpecServicegraph specifications.
    """

    def __init__(
        self,
        source: dict | None = None,
        image: str | None = None,
    ) -> None:
        super().__init__()

        self.image = image
        self.source = source


class FunctionValidatorServicegraph(FunctionValidator):
    """
    FunctionValidatorServicegraph validator.
    """

    source: SourceValidator
    """Source code validator"""

    image: str | None = None
    "Image where the function will be executed"