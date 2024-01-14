#!/usr/bin/env python3
"""
helper function
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
        page: int
        page_size: int
    """
    return (page - 1) * page_size, (page - 1) * page_size + page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page (int): page number. Defaults to 1.
            page_size (int): page size. Defaults to 10.

        Returns:
            List[List]: subset of the file
        """
        assert type(page) == int
        assert type(page_size) == int
        assert int(page) > 0
        assert int(page_size) > 0
        data = self.dataset()

        start = (page - 1) * page_size
        end = page * page_size
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Args:
            page int Defaults to 1.
            page_size int Defaults to 10.
        Returns:
            dict
        """
        data_full = self.dataset()
        data = self.get_page(page, page_size)
        len_lista = len(data_full)
        count_pages = int(len_lista / page_size)
        if (len_lista % page_size > 0):
            count_pages = count_pages + 1
        prev_page = next_page = None
        if (page < count_pages):
            next_page = page + 1
        if (page > 1):
            prev_page = page - 1
        ret = {}
        ret["page_size"] = len(data)
        ret["page"] = page
        ret["data"] = data
        ret["next_page"] = next_page
        ret["prev_page"] = prev_page
        ret["total_pages"] = count_pages

        return ret
