"""Algorithms for Sorting and Searching."""
from __future__ import absolute_import, print_function

from typing import List


def binary_search(arr: List, target: int) -> int:
    """Binary Search.

    Args:
        arr (List): given sorted array.
        target (int): target value.

    Returns:
        int: index in array or -1 if not in array.
    """
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:

        mid = lo + (hi - lo) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            hi = mid - 1

        else:
            lo = mid + 1

    return -1


def search_sorted_rotated(arr: List, target: int) -> int:
    """Search in Sorted and Rotated Array.

    Args:
        arr (List): Given array.
        target (int): targe value.

    Returns:
        int: array index or -1 if not in array.
    """
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:

        mid = lo + (hi - lo) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < arr[-1]:

            if arr[mid] <= target <= arr[-1]:
                lo = mid + 1
            else:
                hi = mid - 1

        else:

            if arr[0] <= target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

    return -1


def bubble_sort(arr: List) -> None:
    """Bubble Sort.

    Args:
        arr (List): given array.
    """
    N = len(arr)
    swapped = False
    for i in range(N):
        for j in range(N - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


def insertion_sort(arr: List) -> None:
    """Run Insertion Sort.

    Args:
        arr (List): given array.
    """
    N = len(arr)
    for i in range(1, N):

        # key = arr[i]

        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

        # if line 90: arr[i] = arr[i-1]
        # arr[i] = key


def merge_sort(arr: List) -> None:
    """Merge Sort.

    Args:
        arr (List): Given array.
    """
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    lt = arr[:mid]
    rt = arr[mid:]

    merge_sort(lt)
    merge_sort(rt)

    lt_ptr, rt_ptr, arr_ptr = 0, 0, 0
    while lt_ptr < len(lt) and rt_ptr < len(rt):

        if lt[lt_ptr] <= rt[rt_ptr]:
            arr[arr_ptr] = lt[lt_ptr]
            lt_ptr += 1
        else:
            arr[arr_ptr] = rt[rt_ptr]
            rt_ptr += 1
        arr_ptr += 1

    while lt_ptr < len(lt):
        arr[arr_ptr] = lt[lt_ptr]
        lt_ptr += 1
        arr_ptr += 1

    # remainder of arr (rt) should already be sorted
    # while rt_ptr < len(rt):
    #    arr[arr_ptr] = rt[rt_ptr]
    #    rt_ptr += 1
    #    arr_ptr += 1


def heap_sort(arr: List) -> None:
    """Heap Sort.

    Args:
        arr (List): given array.
    """

    def heapify(arr, arr_size, index):

        largest = index
        lt = 2 * index + 1
        rt = 2 * index + 2

        if lt < arr_size and arr[largest] < arr[lt]:
            largest = lt

        if rt < arr_size and arr[largest] < arr[rt]:
            largest = rt

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            heapify(arr, arr_size, largest)

    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":

    arr = [2, 3, 4, 10, 40]
    x = 10
    assert binary_search(arr, x) == 3
    x = 15
    assert binary_search(arr, x) == -1

    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    x = 6
    assert search_sorted_rotated(arr, x) == 2
    x = 3
    assert search_sorted_rotated(arr, x) == 8
    x = 10
    assert search_sorted_rotated(arr, x) == -1

    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

    arr = [64, 34, 25, 12, 22, 11, 90]
    heap_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]
