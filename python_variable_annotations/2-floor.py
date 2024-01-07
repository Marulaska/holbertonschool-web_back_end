#!/usr/bin/env python3
"""
type-annotations Floor
"""
from math import floor as fl


def floor(n: float) -> int:
    """
    Args:
        n (float): float number

    Returns:
        int: int number
    """
    r: int = fl(n)
    return r
