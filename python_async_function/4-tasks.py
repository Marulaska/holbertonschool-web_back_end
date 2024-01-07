#!/usr/bin/env python3
"""
async and await syntax
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int)
        max_delay (int)
    Returns:
        List[float]
    """
    list_delay = []
    for i in range(n):
        list_delay.append(await task_wait_random(max_delay))
    return sorted(list_delay)
