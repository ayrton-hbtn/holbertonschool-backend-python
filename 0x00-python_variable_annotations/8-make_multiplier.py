#!/usr/bin/env python3
"""Type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a multiplier of type float and returns a function
    that multiplies a float by multiplier"""
    def m(x: float) -> float:
        """returns the product of multiplier by parameter x"""
        return multiplier * x

    return m
