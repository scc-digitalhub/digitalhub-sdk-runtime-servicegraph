# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum
from typing import ClassVar

from digitalhub.plugins import SourceCode
from pydantic import Field


class Lang(Enum):
    """
    Source code language.
    """

    YAML = "yaml"


class ServicegraphSourceCode(SourceCode):
    """Source code model for Servicegraph functions."""

    DEFAULT_LANG: ClassVar[str | None] = "yaml"
    lang: Lang = Field(default=Lang.YAML.value)
