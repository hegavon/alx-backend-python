#!/usr/bin/env python3
"""
This module contains a function that returns a tuple with a string
and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string `k` and the second
    element is the square of `v` as a float.

    Args:
        k (str): The string element of the tuple.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple with `k` and the square of `v`.
    """
    return (k, float(v ** 2))
