# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations
from open_inference.openapi.client import OpenInferenceClient, InferenceRequest

import json


request = {"inputs": [{"name": "input1", "datatype": "BYTES", "shape": [1], "data": ["prova"]}]}


if __name__ == "__main__":

    client = OpenInferenceClient(base_url='http://localhost:9080')

    # Check that the server is live, and it has the iris model loaded
    client.check_server_readiness()
    client.read_model_metadata('m1')
    pred = client.model_infer(
        "m1",
        request=InferenceRequest(
            inputs=[
                {
                    "name": "input1",
                    "shape": [1],
                    "datatype": "BYTES",
                    "data": [
                        ["prova"],
                        ["prova2"],
                    ],
                }
            ]
        ),
    )

    print(repr(pred))

