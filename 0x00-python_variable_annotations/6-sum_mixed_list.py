#!/usr/bin/env python3
"""Type-annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integers and floats as input and return
    the sum of all the elements as a float"""
    result: float = 0
    for n in mxd_lst:
        if type(n) == int:
            result += float(n)
        else:
            result += n
    return result
