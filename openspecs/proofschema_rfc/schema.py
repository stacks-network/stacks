# -*- coding: utf-8 -*-
"""
    ONS
    ~~~~~

    :copyright: (c) 2014 by ONS
    :license: MIT, see LICENSE for more details.
"""

# v0.1
schema = {
    "name": "Proof",
    "title": "ONS Proof List",
    "type": "array",
    "items": {
        "proof": {
            "type": "object",
            "properties": {
                "rater": "string",
                "ratee": "string",
                "negative": "boolean",
                "date": "string",
                "start": "string",
                "end": "string",
                "object": "string",
                "type": "string",
                "signature": "string"
                }
            }
        }
}
