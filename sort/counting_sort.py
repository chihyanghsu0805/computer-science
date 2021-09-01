"""Implement Counting Sort."""

from __future__ import absolute_import, print_function

from typing import List


def counting_sort(arr: List) -> List:
    """Sort array with counting sort.

    Args:
        arr (List): array to be sorted.

    Returns:
        List: sorted array.
    """
    N = len(arr)
    output = [0] * N
    count = [0] * 256

    for i in arr:
        count[i] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(N):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output
