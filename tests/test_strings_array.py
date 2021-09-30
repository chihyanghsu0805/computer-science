"""Test Strings and Arrays."""

from __future__ import absolute_import, print_function

from algorithms.strings_arrays import (
    convert_zig_zag,
    count_triplets_smaller_sum,
    find_all_palindrome_partitions,
    find_all_palindrome_partitions2,
    find_all_sorted_subarrays,
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
