#!/usr/bin/env python3
"""
module for var with multiple types
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    retuns a tuple of string and square of either int or tuple
    """
    return tuple([k, (v*v)])
