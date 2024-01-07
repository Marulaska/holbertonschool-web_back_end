#!/usr/bin/env python3
"""
type-annotations to kv
"""
from typing import Any, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """

    Args:
        k: (str)
        v: (Union[int, float])

    Returns:
        Dict:[str, Union[float]]
    """
    r: Tuple[str, float] = {k: v**2}
    return r
