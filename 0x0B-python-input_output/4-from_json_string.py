#!/usr/bin/python3
"""Defines a JSON-to-string function."""
import json


def from_json_string(my_str):
    """Returns Object representation of a JSON

    Args:
        my_str (json): The json to be converted
    """
    return json.loads(my_str)
