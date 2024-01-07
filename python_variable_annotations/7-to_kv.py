#!/usr/bin/env python3
"""
type-annotations to kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """

    Args:
        k: (str)
        v: (Union[int, float])

    Returns:
        Dict:[str, Union[float]]
    """
    r: Tuple[str, float] = (k, float(v**2))
    return r
