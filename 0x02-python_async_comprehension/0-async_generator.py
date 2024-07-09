#!/usr/bin/env python3
"""
Module 0-async_generator
This module contains a coroutine that yields a random number.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yields a random number between 0 and 10 after waiting for 1 second,
    10 times.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
