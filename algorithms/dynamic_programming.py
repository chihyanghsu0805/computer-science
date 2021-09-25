"""Dynamic Programming Algortihms."""
from __future__ import absolute_import, print_function

from typing import List, Union


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


def find_longest_common_subsequence2(s1: str, s2: str) -> int:
    """Find Longest Common Subsequence.

    Args:
        s1 (str): first string.
        s2 (str): second string.

    Returns:
        int: length of subsequence
    """
    m = len(s1)
    n = len(s2)

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                curr[j] = 0

            elif s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1

            else:
                curr[j] = max(prev[j], curr[j - 1])

        # Dont use prev = curr
        prev = [i for i in curr]

    return curr[n]


def find_longest_common_subsequence3(s1: str, s2: str) -> Union[int, str]:
    """Find Longest Common Subsequence.

    Args:
        s1 (str): first string.
        s2 (str): second string.

    Returns:
        Union[int, str]: length of subsequence, subsequence
    """
    m = len(s1)
    n = len(s2)

    memo = [[0 for _ in range(n + 1)] for _ in range(2)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                memo[i % 2][j] = 0

            elif s1[i - 1] == s2[j - 1]:
                memo[i % 2][j] = memo[(i + 1) % 2][j - 1] + 1

            else:
                memo[i % 2][j] = max(memo[(i + 1) % 2][j], memo[i % 2][j - 1])

    return memo[i % 2][n]


def find_longest_increasing_subsequence(arr: List) -> int:
    """Find Longest Increasing Subsequence.

    Args:
        arr (List): sequence.

    Returns:
        int: length of subsequence.
    """
    temp = []

    def bin_search(arr, n):

        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == n:
                return mid
            elif arr[mid] < n:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    for n in arr:

        if not temp:
            temp.append(n)

        else:
            if n > temp[-1]:
                temp.append(n)

            else:

                idx = bin_search(temp, n)

                temp[idx] = n

    return len(temp)


def find_minimum_edit(s1: str, s2: str) -> int:
    """Find Minimum Edits.

    Args:
        s1 (str): first string.
        s2 (str): secodn string (fixed).

    Returns:
        int: number of edits.
    """
    m = len(s1)
    n = len(s2)

    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                memo[i][j] = j

            elif j == 0:
                memo[i][j] = i

            elif s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]

            else:
                memo[i][j] = 1 + min(memo[i][j - 1], memo[i - 1][j], memo[i - 1][j - 1])

    return memo[m][n]


def find_minimum_edit2(s1: str, s2: str) -> int:
    """Find Minimum Edits.

    Args:
        s1 (str): first string.
        s2 (str): secodn string (fixed).

    Returns:
        int: number of edits.
    """
    m = len(s1)
    n = len(s2)

    prev = [i for i in range(n + 1)]
    curr = [0 for _ in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(n + 1):

            if j == 0:
                curr[j] = i

            elif s1[i - 1] == s2[j - 1]:

                curr[j] = prev[j - 1]

            else:
                curr[j] = 1 + min(curr[j - 1], prev[j], prev[j - 1])

        # Dont use prev = curr
        prev = [i for i in curr]

    return prev[n]


def find_minimum_edit3(s1: str, s2: str) -> int:
    """Find Minimum Edits.

    Args:
        s1 (str): first string.
        s2 (str): secodn string (fixed).

    Returns:
        int: number of edits.
    """
    m = len(s1)
    n = len(s2)

    # m columns since s2 is fixed
    memo = [[0 for _ in range(m + 1)] for _ in range(2)]

    for i in range(m + 1):
        memo[0][i] = i

    # First
    for i in range(1, n + 1):
        for j in range(m + 1):

            # Use i % 2 to distinguish prev and curr
            if j == 0:
                memo[i % 2][j] = i

            elif s1[j - 1] == s2[i - 1]:
                memo[i % 2][j] = memo[(i - 1) % 2][j - 1]

            else:
                memo[i % 2][j] = 1 + min(
                    memo[(i - 1) % 2][j], memo[i % 2][j - 1], memo[(i - 1) % 2][j - 1]
                )

    return memo[n % 2][m]


def find_minimum_partition_sum(arr: List) -> int:
    """Find Minimum Partition Sum.

    Args:
        arr (List): array.

    Returns:
        int: minimum.
    """
    _sum = sum(arr)
    N = len(arr)

    dp = [[0 for _ in range(_sum + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = True

    for j in range(1, _sum + 1):
        dp[0][j] = False

    for i in range(1, N + 1):
        for j in range(1, _sum + 1):

            dp[i][j] = dp[i - 1][j]

            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] | dp[i - 1][j - arr[i - 1]]

    diff = _sum

    for j in range(_sum // 2, -1, -1):
        if dp[N][j]:
            diff = _sum - j - j
            break

    return diff


def find_minimum_partition_sum2(arr: List) -> int:
    """Find Minimum Partition Sum.

    Args:
        arr (List): array.

    Returns:
        int: minimum.
    """
    _sum = sum(arr)
    N = len(arr)

    prev = [False for _ in range(_sum + 1)]
    prev[0] = True

    curr = [False for _ in range(_sum + 1)]
    curr[0] = True

    for i in range(1, N + 1):
        for j in range(1, _sum + 1):

            curr[j] = prev[j]

            if arr[i - 1] <= j:
                curr[j] = curr[j] | prev[j - arr[i - 1]]

        prev = [i for i in curr]

    diff = _sum

    for j in range(_sum // 2, -1, -1):
        if prev[j]:
            diff = _sum - j - j
            break

    return diff


def count_number_ways(n: int) -> int:
    """Count Number of Ways.

    Args:
        n (int): number of step.

    Returns:
        int: number of ways.
    """
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def count_number_ways2(n: int) -> int:
    """Count Number of Ways.

    Args:
        n (int): number of step.

    Returns:
        int: number of ways.
    """
    dp = [0] * 3

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3] + dp[(i - 3) % 3]

    return dp[n % 3]


def find_longest_path(matrix: List) -> int:
    """Find Longest Path.

    Args:
        matrix (List): grid of unique integers.

    Returns:
        int: longest path.
    """
    m = len(matrix)
    n = len(matrix[0])
    longest_path = 1
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    def valid_cell(r, c):
        if r < 0 or c < 0 or r > m - 1 or c > n - 1:
            return False
        return True

    def find_path(r, c):

        if not valid_cell(r, c):
            return 0

        if dp[r][c] != -1:
            return dp[r][c]

        nbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        current = 1
        for dr, dc in nbors:

            if valid_cell(r + dr, c + dc):

                if matrix[r + dr][c + dc] - matrix[r][c] == 1:
                    temp = 1 + find_path(r + dr, c + dc)
                    current = max(temp, current)

        dp[r][c] = current
        return dp[r][c]

    for r in range(m):
        for c in range(n):

            if dp[r][c] == -1:
                find_path(r, c)

            longest_path = max(longest_path, dp[r][c])

    return longest_path


def find_subset_sum(arr: List, target: int) -> bool:
    """Find Subset Sum.

    Args:
        arr (List): given array.
        target (int): target sum.

    Returns:
        bool: sum found.
    """
    N = len(arr)

    dp = [[False for _ in range(target + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, target + 1):

            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            elif j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[-1][target], dp


def find_subset_sum2(arr: List, target: int) -> bool:
    """Find Subset Sum.

    Args:
        arr (List): given array.
        target (int): target sum.

    Returns:
        bool: sum found.
    """
    N = len(arr)

    dp = [[False for _ in range(target + 1)] for _ in range(2)]

    for i in range(N + 1):
        for j in range(target + 1):

            if j == 0:
                dp[i % 2][j] = True

            elif i == 0:
                dp[i % 2][j] = False

            elif arr[i - 1] > j:
                dp[i % 2][j] = dp[(i + 1) % 2][j]

            elif j >= arr[i - 1]:
                dp[i % 2][j] = dp[(i + 1) % 2][j] or dp[(i + 1) % 2][j - arr[i - 1]]

    return dp[i % 2][target]


def find_all_subsets(
    arr: List, index: int, target: int, path: List, subset: List, result: List
):
    """Find All Subsets.

    Args:
        arr (List): given array.
        index (int): row index in subset matrix.
        target (int): target sum.
        path (List): path to target sum.
        subset (List): subset matrix.
        result (List): subset that sums to target.
    """
    if index == 0 and target != 0 and subset[0][target]:
        path.append(arr[index])
        result.append(path)
        return

    if index == 0 and target == 0:
        result.append(path)
        return

    if subset[index - 1][target]:
        find_all_subsets(arr, index - 1, target, path, subset, result)

    if target >= arr[index - 1] and subset[index][target - arr[index - 1]]:
        find_all_subsets(
            arr,
            index - 1,
            target - arr[index - 1],
            path + [arr[index - 1]],
            subset,
            result,
        )


def play_coin_game(arr: List) -> int:
    """Play Coin Game.

    Args:
        arr (List): array of coins.

    Returns:
        int: optimal value.
    """
    N = len(arr)

    table = [[0 for _ in range(N)] for _ in range(N)]

    for gap in range(N):
        for j in range(gap, N):

            # Base case:
            # F[i][j] = Vi if j==i
            # F[i][j] = max(Vi, Vj) if j==i+1
            i = j - gap

            x, y, z = 0, 0, 0
            if 2 <= gap:
                # F[i+2][j], if player took i, opponent took i+1
                x = table[i + 2][j]
                # F[i+1][j-1], if player took j, opponent took i or vice versa
                y = table[i + 1][j - 1]
                # F[i+2][j], if player took j, opponent took j-1
                z = table[i][j - 2]

            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))

    return table[0][N - 1]


if __name__ == "__main__":

    X = "AGGTAB"
    Y = "GXTXAYB"

    assert find_longest_common_subsequence(X, Y)[0] == 4
    assert find_longest_common_subsequence(X, Y)[1] == "GTAB"
    assert find_longest_common_subsequence2(X, Y) == 4
    assert find_longest_common_subsequence3(X, Y) == 4

    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == 5

    str1 = "sunday"
    str2 = "saturday"

    assert find_minimum_edit(str1, str2) == 3
    assert find_minimum_edit2(str1, str2) == 3
    assert find_minimum_edit3(str1, str2) == 3

    arr = [3, 1, 4, 2, 2, 1]
    assert find_minimum_partition_sum(arr) == 1
    assert find_minimum_partition_sum2(arr) == 1

    n = 4
    assert count_number_ways(n) == 7
    assert count_number_ways2(n) == 7

    m = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
    assert find_longest_path(m) == 4

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

    arr = [8, 15, 3, 7]
    assert play_coin_game(arr) == 22
    arr = [2, 2, 2, 2]
    assert play_coin_game(arr) == 4

    arr = [20, 30, 2, 2, 2, 10]
    assert play_coin_game(arr) == 42
