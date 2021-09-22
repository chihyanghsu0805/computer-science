"""Implement Counting Sort."""

from __future__ import absolute_import, print_function

from typing import List


def counting_sort(arr: List, exp: int = 1) -> List:
    """Sort array with counting sort.

    Args:
        arr (List): array to be sorted.
        exp (int, optional): exponent. Defaults to 1.

    Returns:
        List: sorted array.
    """
    N = len(arr)
    output = [0] * N

    count = [0] * 10

    for i in range(N):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = N - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    return output
