#!/usr/bin/env python3
"""Type-annotated function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v, returns a tuple
    with the k as the first element and the square of v as a float
    as the second element"""
    if type(v) == int:
        float(v)
    return (k, v**2)
