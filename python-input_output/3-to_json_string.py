#!/usr/bin/python3
"""Defines a function to convert Python objects to JSON strings."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
