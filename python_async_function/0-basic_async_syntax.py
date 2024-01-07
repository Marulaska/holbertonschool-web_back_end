#!/usr/bin/env python3
"""
async and await syntax
"""
import asyncio
import random
from typing import Optional

async def wait_random(max_delay: Optional[float] = 10) -> float:
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
