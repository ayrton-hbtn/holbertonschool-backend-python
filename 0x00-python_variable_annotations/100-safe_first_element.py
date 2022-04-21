#!/usr/bin/env python3
"""Type-annotated function"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns the first element of list, safely """
    if lst:
        return lst[0]
    else:
        return None
