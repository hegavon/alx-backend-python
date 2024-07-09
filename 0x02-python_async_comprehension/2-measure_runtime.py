#!/usr/bin/env python3
"""
Module 2-measure_runtime
This module contains a coroutine that measures the total runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime of executing async_comprehension four times
    in parallel.
    '''
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
