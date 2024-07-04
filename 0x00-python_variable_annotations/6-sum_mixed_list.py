#!/usr/bin/env python3
"""
This module contains a function that sums a list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats to sum

    Returns:
        float: The sum of the list as a float
    """
    return sum(mxd_lst)
