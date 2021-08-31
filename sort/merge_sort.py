"""Implement merge sort."""

from __future__ import absolute_import, print_function

from typing import List


def merge_sort(arr: List) -> List:
    """Sort array using merge sort.

    Args:
        arr (List): array to be sorted.

    Returns:
        List: sorted array.
    """
    if not arr:
        return arr

    if len(arr) > 1:
        mid = len(arr) // 2
        lt = arr[:mid]
        rt = arr[mid:]

        merge_sort(lt)
        merge_sort(rt)

        merge(arr, lt, rt)


def merge(arr: List, lt: List, rt: List):
    """Merge left and right arrays.

    Args:
        arr (List): original array.
        lt (List): left partition.
        rt (List): right partition.
    """
    i, j, k = 0, 0, 0

    while (i < len(lt)) and (j < len(rt)):
        if lt[i] < rt[j]:
            arr[k] = lt[i]
            i += 1
        else:
            arr[k] = rt[j]
            j += 1
        k += 1

    while i < len(lt):
        arr[k] = lt[i]
        i += 1
        k += 1

    while j < len(rt):
        arr[k] = rt[j]
        j += 1
        k += 1
