"""Implement Bubble Sort."""

from typing import List


def bubble_sort(arr: List):
    """Sort array using bubble sort.

    Args:
        arr (List): array to be sorted.
    """
    N = len(arr)

    for i in range(N):
        swapped = False
        for j in range(0, N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
