"""Test Dynamic Programming Algorithms."""
from __future__ import absolute_import, print_function

from algorithms.dynamic_programming import (
    count_number_ways,
    count_number_ways2,
    evaluate_boolean,
    evaluate_boolean2,
    fill_knapsack,
    fill_knapsack2,
    find_all_subsets,
    find_longest_common_subsequence,
    find_longest_common_subsequence2,
    find_longest_common_subsequence3,
    find_longest_increasing_subsequence,
    find_longest_path,
    find_minimum_edit,
    find_minimum_edit2,
    find_minimum_edit3,
    find_minimum_partition_sum,
    find_subset_sum,
    find_subset_sum2,
    play_coin_game,
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


def test_count_number_ways():
    """Test Count Number of Ways."""
    n = 4
    assert count_number_ways(n) == 7
    assert count_number_ways2(n) == 7


def test_find_longest_path():
    """Test Find Longest Path."""
    m = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
    assert find_longest_path(m) == 4


def test_find_subset_sum():
    """Test Find Subset Sum."""
    arr = [3, 34, 4, 12, 5, 2]
    _sum = 9
    assert find_subset_sum(arr, _sum)[0]
    dp = find_subset_sum(arr, _sum)[1]
    subsets = []
    find_all_subsets(arr, len(arr), _sum, [], dp, subsets)
    assert all(sum(sub) == _sum for sub in subsets)
    assert find_subset_sum2(arr, _sum)

    _sum = 30
    assert not find_subset_sum(arr, _sum)[0]
    assert not find_subset_sum2(arr, _sum)


def test_play_coin_game():
    """Test Play Coin Game."""
    arr = [8, 15, 3, 7]
    assert play_coin_game(arr) == 22

    arr = [2, 2, 2, 2]
    assert play_coin_game(arr) == 4

    arr = [20, 30, 2, 2, 2, 10]
    assert play_coin_game(arr) == 42


def test_fill_knapsack():
    """Test Fill Knapsack."""
    v = [60, 100, 120]
    w = [10, 20, 30]
    W = 50
    assert fill_knapsack(w, v, W) == 220
    assert fill_knapsack2(w, v, W) == 220


def test_evaluate_boolean():
    """Test Evaluate Boolean."""
    symbols = "TTFT"
    operators = "|&^"
    assert evaluate_boolean(symbols, operators) == 4
    assert evaluate_boolean2(symbols, operators) == 4
