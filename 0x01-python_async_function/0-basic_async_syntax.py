#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
This module contains a single coroutine that waits for a random delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (inclusive) seconds and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The amount of time in seconds it waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
