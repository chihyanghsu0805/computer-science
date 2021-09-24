"""Dynamic Programming Algortihms."""
from __future__ import absolute_import, print_function

from typing import Union


def find_longest_common_subsequence(s1: str, s2: str) -> Union[int, str]:
    """Find Longest Common Subsequence.

    Args:
        s1 (str): first string.
        s2 (str): second string.

    Returns:
        Union[int, str]: length of subsequence, subsequence
    """
    m = len(s1)
    n = len(s2)

    memo = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                memo[i][j] = 0

            elif s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1

            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    s = ""

    i = m
    j = n

    while i > 0 and j > 0:

        if s1[i - 1] == s2[j - 1]:
            s += s1[i - 1]
            i -= 1
            j -= 1

        elif memo[i - 1][j] > memo[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return memo[m][n], s[::-1]


def find_longest_common_subsequence2(s1: str, s2: str) -> Union[int, str]:
    """Find Longest Common Subsequence.

    Args:
        s1 (str): first string.
        s2 (str): second string.

    Returns:
        Union[int, str]: length of subsequence, subsequence
    """
    m = len(s1)
    n = len(s2)

    prev = [None] * (n + 1)
    curr = [None] * (n + 1)

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                curr[j] = 0

            elif s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1

            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev = curr

    return curr[n]


if __name__ == "__main__":

    X = "AGGTAB"
    Y = "GXTXAYB"

    assert find_longest_common_subsequence(X, Y)[0] == 4
    assert find_longest_common_subsequence(X, Y)[1] == "GTAB"
    assert find_longest_common_subsequence2(X, Y) == 4
