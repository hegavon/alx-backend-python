#!/usr/bin/env python3
"""
Module 4-tasks
This module contains a function that spawns task_wait_random n times
and returns the list of delays in ascending order
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns tax_wait n times with the specified max_delay and returns the
    list of all the delays in ascending order without using sort()
    '''
    tasks = []
    delays = []

    # Create tasks
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    # Await tasks and collect results
    for task in tasks:
        result = await task
        delays.append(result)

    return sorted(delays)
