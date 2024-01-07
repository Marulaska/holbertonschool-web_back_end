#!/usr/bin/env python3
"""
async and await syntax
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int)
        max_delay (int)

    Returns:
        List[float]
    """
    delays: List[float] = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
