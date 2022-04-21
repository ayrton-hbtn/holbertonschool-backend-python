#!/usr/bin/env python3
"""Type-annotated function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats as input and return
    the total sum of the elements from the list"""
    result: float = 0
    for n in input_list:
        result += n
    return result
