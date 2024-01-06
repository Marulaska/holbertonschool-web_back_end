#!/usr/bin/env python3
"""
type-annotations Sum mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """

    Args:
        mxd_lst: (List[Union[int, float]]):

    Returns:
        Union[int, float]
    """
    r: Union[int, float] = sum(mxd_lst)
    return r
