"""Test Dynamic Programming Algorithms."""
from __future__ import absolute_import, print_function

from algorithms.dynamic_programming import (
    find_longest_common_subsequence,
    find_longest_common_subsequence2,
    find_longest_common_subsequence3,
    find_longest_increasing_subsequence,
    find_minimum_edit,
    find_minimum_edit2,
    find_minimum_edit3,
    find_minimum_partition_sum,
)


def test_longest_common_subsequence():
    """Test Longest Common Subsequence."""
    X = "AGGTAB"
    Y = "GXTXAYB"

    assert find_longest_common_subsequence(X, Y)[0] == 4
    assert find_longest_common_subsequence(X, Y)[1] == "GTAB"
    assert find_longest_common_subsequence2(X, Y) == 4
    assert find_longest_common_subsequence3(X, Y) == 4


def test_longest_increasing_subsequence():
    """Test Longest Increasing Subsequence."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == 5


def test_find_minimum_edit():
    """Test Minimum Edit."""
    str1 = "sunday"
    str2 = "saturday"

    assert find_minimum_edit(str1, str2) == 3
    assert find_minimum_edit2(str1, str2) == 3
    assert find_minimum_edit3(str1, str2) == 3


def test_find_minimum_partition_sum():
    """Test Minimum Partition Sum."""
    arr = [3, 1, 4, 2, 2, 1]
    assert find_minimum_partition_sum(arr) == 1