"""Test Strings and Arrays."""

from __future__ import absolute_import, print_function

from algorithms.strings_arrays import (
    convert_zig_zag,
    count_triplets_smaller_sum,
    find_all_palindrome_partitions,
    find_all_palindrome_partitions2,
    find_all_sorted_subarrays,
    find_longest_contiguous_subarray,
    find_longest_contiguous_subarray2,
    find_pythagorean,
    find_smallest_number_not_sum,
    find_smallest_subarray_greater_sum,
    maximize_profit,
    maximize_profit2,
    reverse_ignore_special,
)


def test_reverse_array_ignore_special():
    """Test Reverse Array Ignore Special."""
    s = "a!!!b.c.d,e'f,ghi"
    assert reverse_ignore_special(s) == "i!!!h.g.f,e'd,cba"


def test_find_all_palindrome_partitions():
    """Test Find All Palindrome Partitions."""
    s = "nitin"
    assert find_all_palindrome_partitions(s) == [
        ["n", "i", "t", "i", "n"],
        ["n", "iti", "n"],
        ["nitin"],
    ]
    assert find_all_palindrome_partitions2(s) == [
        "n",
        "i",
        "t",
        "iti",
        "nitin",
        "i",
        "n",
    ]

    s = "geeks"
    assert find_all_palindrome_partitions(s) == [
        ["g", "e", "e", "k", "s"],
        ["g", "ee", "k", "s"],
    ]
    assert find_all_palindrome_partitions2(s) == ["g", "e", "ee", "e", "k", "s"]


def test_count_triplets_smaller_sum():
    """Test Count Triplets Smaller Sum."""
    arr = [5, 1, 3, 4, 7]
    assert count_triplets_smaller_sum(arr, 12) == 4


def test_convert_zig_zag():
    """Test Convert Zig Zag."""
    arr = [4, 3, 7, 8, 6, 2, 1]
    convert_zig_zag(arr)
    assert arr == [4, 7, 3, 8, 2, 6, 1]


def test_find_all_sorted_subarrays():
    """Test Find All Sorted Subarrays."""
    arr1 = [10, 15, 25]
    arr2 = [5, 20, 30]
    assert find_all_sorted_subarrays(arr1, arr2) == [
        [10, 20],
        [10, 20, 25, 30],
        [10, 30],
        [15, 20],
        [15, 20, 25, 30],
        [15, 30],
        [25, 30],
    ]


def test_find_pythagorean():
    """Test Find Pythagorean."""
    arr = [3, 1, 4, 6, 5]
    assert find_pythagorean(arr)


def test_find_longest_contiguous_subarray():
    """Test Find Longest Contiguous Subarray."""
    arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
    assert find_longest_contiguous_subarray(arr) == 5
    arr = [10, 12, 12, 10, 10, 11, 10]
    assert find_longest_contiguous_subarray2(arr) == 2


def test_find_smallest_subarray_greater_sum():
    """Test Find Smallest Subarray Greater Sum."""
    arr = [1, 4, 45, 6, 10, 19]
    K = 51
    assert find_smallest_subarray_greater_sum(arr, K) == 3
    arr = [1, 10, 5, 2, 7]
    K = 9
    assert find_smallest_subarray_greater_sum(arr, K) == 1
    arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    K = 280
    assert find_smallest_subarray_greater_sum(arr, K) == 4


def test_maximize_profit():
    """Test Maximize Profit."""
    price = [100, 180, 260, 310, 40, 535, 695]
    assert maximize_profit(price) == 865
    assert maximize_profit2(price) == [(0, 3), (4, 6)]


def test_find_smallest_number_not_sum():
    """Test Find Smallest Number Not Sum."""
    arr = [1, 3, 4, 5]
    assert find_smallest_number_not_sum(arr) == 2
    arr = [1, 2, 6, 10, 11, 15]
    assert find_smallest_number_not_sum(arr) == 4
    arr = [1, 1, 1, 1]
    assert find_smallest_number_not_sum(arr) == 5
    arr = [1, 1, 3, 4]
    assert find_smallest_number_not_sum(arr) == 10
