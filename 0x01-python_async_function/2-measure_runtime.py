#!/usr/bin/env python3
"""
Module 2-measure_runtime
This module contains a function that measures the runtime of wait_n.
"""

import asyncio
import time
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per call.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
