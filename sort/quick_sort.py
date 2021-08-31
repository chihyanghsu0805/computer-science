"""Implement Quick Sort."""

from __future__ import absolute_import, print_function

from typing import List


def quick_sort(arr: List, lo: int = 0, hi: int = None) -> None:
    """Sort array with quick sort.

    Args:
        arr (List): array to be sorted.
        lo (int, optional): index of start of array. Defaults to 0.
        hi (int, optional): index of end of array. Defaults to None.
    """
    if hi is None:
        hi = len(arr) - 1

    if lo < hi:
        pi = partition(arr, lo, hi)

        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)


def partition(arr: List, lo: int, hi: int) -> int:
    """Partition the array with pivot.

    Args:
        arr (List): original array.
        lo (int): index of start of array.
        hi (int): index of end of array.

    Returns:
        int: pivot index.
    """
    # latest index with value smaller than pivot,
    # with next index with value bigger than pivot.
    i = lo - 1

    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1  # move to index with value bigger than index.
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot and index so all values to left of pivot is smaller.
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

    return i + 1
