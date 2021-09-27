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


def quick_sort(arr: List, lo: int, hi: int) -> None:
    """Run Quick Sort.

    Args:
        arr (List): Given array.
        lo (int): start index.
        hi (int): end index.
    """

    def partition(arr, lo, hi):
        # Hoare's

        pivot_index = lo
        pivot_value = arr[pivot_index]

        while lo < hi:

            while lo < len(arr) and arr[lo] <= pivot_value:
                lo += 1

            while arr[hi] > pivot_value:
                hi -= 1

            if lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]

        arr[hi], arr[pivot_index] = arr[pivot_index], arr[hi]

        return hi

    if lo < hi:
        idx = partition(arr, lo, hi)

        quick_sort(arr, lo, idx - 1)
        quick_sort(arr, idx + 1, hi)


def interpolation_search(arr: List, target: int, lo: int, hi: int) -> int:
    """Run Interpolation Search.

    Args:
        arr (List): Given array.
        target (int): target value.
        lo (int): start index.
        hi (int): end index.

    Returns:
        int: array index, -1 if not found.
    """
    if target < arr[lo] or target > arr[hi]:
        return -1

    if hi < lo:
        return -1

    idx = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (target - arr[lo]))

    if arr[idx] == target:
        return idx
    elif arr[idx] < target:
        return interpolation_search(arr, target, idx + 1, hi)
    else:
        return interpolation_search(arr, target, lo, idx - 1)


def interpolation_search2(arr: List, target: int) -> int:
    """Run Interpolation Search.

    Args:
        arr (List): Given array.
        target (int): target value.
        lo (int): start index.
        hi (int): end index.

    Returns:
        int: array index, -1 if not found.
    """
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:

        if hi == lo:
            idx = hi
        else:
            idx = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))

        if arr[idx] == target:
            return idx
        elif arr[idx] < target:
            lo = idx + 1
        else:
            hi = idx - 1

    return -1


def quick_select(arr: list, K: int) -> int:
    """Quick Select.

    Args:
        arr (list): Given array.
        K (int): Kth.

    Returns:
        int: array index.
    """

    def partition(arr, lo, hi):
        # Lomuto's

        pivot_index = lo + (hi - lo) // 2
        pivot_value = arr[pivot_index]

        arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
        store_index = lo
        for i in range(lo, hi):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[store_index], arr[hi] = arr[hi], arr[store_index]
        return store_index

    lo, hi = 0, len(arr) - 1

    while lo <= hi:

        if lo == hi:
            return arr[lo]

        pivot_index = partition(arr, lo, hi)
        if pivot_index == K:
            return arr[pivot_index]
        elif pivot_index < K:
            lo = pivot_index + 1
        else:
            hi = pivot_index - 1

    return -1


def find_pair_closest_sum(arr: List, target: int) -> List:
    """Find pair with Closest Sum.

    Args:
        arr (List): Given array.
        target (int): Target sum.

    Returns:
        List: array indices.
    """
    lt, rt = 0, len(arr) - 1

    min_diff = float("inf")

    while lt < rt:

        diff = abs(arr[lt] + arr[rt] - target)
        if diff < min_diff:
            min_diff = diff
            pair = [lt, rt]

        if arr[lt] + arr[rt] > target:
            rt -= 1

        else:
            lt += 1

    return pair


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

    arr = [64, 34, 25, 12, 22, 11, 90]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

    arr = [2, 3, 4, 10, 40]
    x = 10
    assert interpolation_search(arr, x, 0, len(arr) - 1) == 3
    assert interpolation_search2(arr, x) == 3
    x = 15
    assert interpolation_search(arr, x, 0, len(arr) - 1) == -1
    assert interpolation_search2(arr, x) == -1

    arr = [64, 34, 25, 12, 22, 11, 90]
    temp = [quick_select(arr, i) for i in range(0, len(arr))]
    assert temp == sorted(arr)

    arr = [10, 22, 28, 29, 30, 40]
    x = 54
    assert find_pair_closest_sum(arr, x) == [1, 4]
    x = 56
    assert find_pair_closest_sum(arr, x) == [2, 3]
