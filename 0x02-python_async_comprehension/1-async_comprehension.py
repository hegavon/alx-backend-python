#!/usr/bin/env python3
"""
Module 1-async_comprehension
This module contains a coroutine that collects random numbers using an async
comprehension.
"""

import asyncio
from typing import List


# Importing async_generator from the previous module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehension over
    async_generator.
    '''
    return [number async for number in async_generator()]
