"""Implement Selection Sort."""

from typing import List


def selection_sort(arr: List) -> None:
    """Sort list with selection sort.

    Args:
        arr (List): list to be sorted.
    """
    N = len(arr)
    for i in range(N):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # Stable
        key = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1

        arr[i] = key
