#!/usr/bin/env python3
"""
Module 4-tasks
This module contains a function that spawns task_wait_random n times
and returns the list of delays in ascending order.
"""

import asyncio
from typing import List

# Importing task_wait_random from the previous module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times and returns sorted wait times.
    '''
    # Using asyncio.gather to execute task_wait_random(max_delay) n times
    wait_times = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    )
    return sorted(wait_times)
