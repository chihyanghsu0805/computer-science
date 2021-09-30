"""Test Sort and Search."""

from __future__ import absolute_import, print_function

from algorithms.sort_search import (
    binary_search,
    bubble_sort,
    find_pair_closest_sum,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_select,
    quick_sort,
    search_sorted_rotated,
)


def test_binary_search():
    """Test Binary Search."""
    arr = [2, 3, 4, 10, 40]
    x = 10
    assert binary_search(arr, x) == 3
    x = 15
    assert binary_search(arr, x) == -1


def test_search_sorted_rotated():
    """Test Search Sorted Rotated."""
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    x = 6
    assert search_sorted_rotated(arr, x) == 2
    x = 3
    assert search_sorted_rotated(arr, x) == 8
    x = 10
    assert search_sorted_rotated(arr, x) == -1


def test_bubble_sort():
    """Test Bubble Sort."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]


def test_insertion_sort():
    """Test Insertion Sort."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]


def test_merge_sort():
    """Test Merge Sort."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]


def test_heap_sort():
    """Test Heap Sort."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    heap_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]


def test_quick_sort():
    """Test Quick Sort."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [11, 12, 22, 25, 34, 64, 90]


def test_quick_select():
    """Test Quick Select."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    temp = [quick_select(arr, i) for i in range(0, len(arr))]
    assert temp == sorted(arr)


def test_find_pair_closest_sum():
    """Test Find Pair Closest Sum."""
    arr = [10, 22, 28, 29, 30, 40]
    x = 54
    assert find_pair_closest_sum(arr, x) == [1, 4]
    x = 56
    assert find_pair_closest_sum(arr, x) == [2, 3]
