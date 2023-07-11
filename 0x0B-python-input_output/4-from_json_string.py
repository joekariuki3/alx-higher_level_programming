#!/usr/bin/python3
"""
import json module
"""

import json

"""
fuction to convert json to string
"""


def from_json_string(my_str):
    """
    convert my_str json to object
    """
    return json.loads(my_str)
