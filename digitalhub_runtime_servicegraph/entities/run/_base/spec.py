# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunSpecFunction


class RunSpecServicegraphRun(RunSpecFunction):
    """RunSpecServicegraphRun specifications."""

    source: dict | None = None
    image: str | None = None
    parameters: dict | None = None
