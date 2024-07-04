#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: It multiplies its float input by `multiplier`
    """
    def multiply(n: float) -> float:
        """Multiplies `n` by the multiplier."""
        return n * multiplier

    return multiply
