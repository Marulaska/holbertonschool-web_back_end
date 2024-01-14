#!/usr/bin/env python3
"""
helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
        page: int
        page_size: int
    """
    return (page - 1) * page_size, (page - 1) * page_size + page_size
