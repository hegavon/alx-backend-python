#!/usr/bin/env python3
"""
This module contains a function that returns tuples of elements & their lengths
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from its length

    Args:
        lst (Iterable[Sequence]): A list or iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing an element
                                    from lst and its corresponding length
    """
    return [(i, len(i)) for i in lst]
