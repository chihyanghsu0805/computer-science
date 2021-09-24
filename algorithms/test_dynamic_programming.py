"""Test Dynamic Programming Algorithms."""
from __future__ import absolute_import, print_function

from algorithms.dynamic_programming import (
    find_longest_common_subsequence,
    find_longest_common_subsequence2,
    find_longest_increasing_subsequence,
)


def test_longest_common_subsequence():
    """Test Longest Common Subsequence."""
    X = "AGGTAB"
    Y = "GXTXAYB"

    assert find_longest_common_subsequence(X, Y)[0] == 4
    assert find_longest_common_subsequence(X, Y)[1] == "GTAB"
    assert find_longest_common_subsequence2(X, Y) == 4


def test_longest_increasing_subsequence():
    """Test Longest Increasing Subsequence."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == 5
