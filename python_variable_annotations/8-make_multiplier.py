#!/usr/bin/env python3
"""
type-annotations make multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        x: (float)
    """
    def func_multiplier(value: float) -> float:
        """
        Args:
            y: (float)
        """
        return value * multiplier
    return func_multiplier
