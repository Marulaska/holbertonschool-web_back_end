#!/usr/bin/env python3
"""
type-annotations element length
"""
from typing import Iterable, Sequence, List, Tuple



def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst: (Iterable, Sequence)

    Returns:
        List:[Tuple[str, int]]S
    """
    return [(i, len(i)) for i in lst]
