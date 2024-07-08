#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
This module contains a coroutine that spawns wait_random n times and returns
the list of delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns wait_random n times with the specified max_delay and returns the
    list of all the delays in ascending order without using sort().
    '''
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
        # Insert the delay in the correct position to maintain ascending order
        for i in range(len(delays) - 1, 0, -1):
            if delays[i] < delays[i - 1]:
                delays[i], delays[i - 1] = delays[i - 1], delays[i]
            else:
                break
    return delays
