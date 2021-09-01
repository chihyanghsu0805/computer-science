"""Implement Radix Sort."""

from __future__ import absolute_import, print_function

from typing import List

from counting_sort import counting_sort


def radix_sort(arr: List) -> List:
    """Sort array with radix sort.

    Args:
        arr (List): array to be sorted.

    Returns:
        List: sorted array.
    """
    max_value = max(arr)
    exp = 1
    while max_value / exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr
