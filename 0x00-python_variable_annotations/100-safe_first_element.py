#!/usr/bin/env python3
"""
This contains a function that safely retrieves the first element of a list
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieves the first element of a list.

    Args:
        lst (Sequence): A sequence (list, tuple, etc.) of elements.

    Returns:
        Union[Any, None]: The first element of the list if it exists
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
