"""Algorithmgs for Strings and Arrays."""

from __future__ import absolute_import, print_function

from typing import List


def reverse_ignore_special(arr: str) -> str:
    """Reverse Ignoring Special Characters.

    Args:
        arr (str): given string.

    Returns:
        str: reversed string.
    """
    arr = list(arr)

    forward = 0
    backward = len(arr) - 1

    while forward < backward:

        while not arr[forward].isalpha():
            forward += 1

        while not arr[backward].isalpha():
            backward -= 1

        arr[backward], arr[forward] = arr[forward], arr[backward]
        backward -= 1
        forward += 1

    return "".join(arr)


def is_palindrome(s: str) -> bool:
    """Check String is Palindrome.

    Args:
        s (str): given string.

    Returns:
        bool: True if string is palindrome.
    """
    f_ptr = 0
    b_ptr = len(s) - 1

    while f_ptr < b_ptr:

        if s[f_ptr] != s[b_ptr]:
            return False

        f_ptr += 1
        b_ptr -= 1

    return True


def find_all_palindrome_partitions(s: str) -> List:
    """Find All Palindrome Partitions.

    Args:
        s (str): given string.

    Returns:
        List: list of palindrome paritions.
    """
    all_partition = []
    curr_partition = []

    def helper(all, curr, start, n, s):

        if start >= n:
            x = curr.copy()
            all.append(x)
            return

        for i in range(start, n):
            sub_s = s[start : i + 1]
            if is_palindrome(sub_s):
                curr.append(sub_s)
                helper(all, curr, i + 1, n, s)
                curr.pop()

    helper(all_partition, curr_partition, 0, len(s), s)
    return all_partition


def find_all_palindrome_partitions2(s: str) -> List:
    """Find All Palindromes.

    Args:
        s (str): given string.

    Returns:
        List: list of palindromes.
    """
    all_p = []

    def find_palindrome(s, i, j):
        if i < 0 or j > len(s) - 1:
            return

        while i >= 0 and j < len(s) and s[i] == s[j]:
            all_p.append(s[i : j + 1])
            i -= 1
            j += 1

    for i in range(len(s)):
        find_palindrome(s, i, i)
        find_palindrome(s, i, i + 1)

    return all_p


def count_triplets_smaller_sum(arr: List, N: int) -> int:
    """Count Triplets with Smaller Sum.

    Args:
        arr (List): array with numbers.
        N (int): Target Sum.

    Returns:
        int: Number of Triplets.
    """
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):

        j = i + 1
        k = len(arr) - 1

        while j < k:

            if arr[i] + arr[j] + arr[k] >= N:
                k -= 1

            else:
                count += k - j
                j = j + 1

    return count


def convert_zig_zag(arr: List) -> None:
    """Convert Zig Zag.

    Args:
        arr (List): given array.
    """
    N = len(arr)

    for i in range(1, N, 2):

        sub = arr[i - 1 : i + 2]

        if arr[i] == max(sub):
            continue
        else:
            if arr[i - 1] == max(sub):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def find_all_sorted_subarrays(arr1: List, arr2: List) -> List:
    """Find All Sorted Subarrays.

    Args:
        arr1 (List): first array.
        arr2 (List): second array.

    Returns:
        List: sorted subarrays.
    """
    M = len(arr1)
    N = len(arr2)

    C = [0] * (M + N + 1)
    all = []

    def helper(a_ptr, b_ptr, c_ptr, a_bool):

        if a_bool:

            if c_ptr:
                all.append(C[: c_ptr + 1].copy())

            for i in range(a_ptr, M):

                if not c_ptr:
                    C[c_ptr] = arr1[i]
                    helper(i + 1, b_ptr, c_ptr, not a_bool)
                else:
                    if arr1[i] > C[c_ptr]:
                        C[c_ptr + 1] = arr1[i]
                        helper(i + 1, b_ptr, c_ptr + 1, not a_bool)
        else:
            for j in range(b_ptr, N):
                if arr2[j] > C[c_ptr]:
                    C[c_ptr + 1] = arr2[j]
                    helper(a_ptr, j + 1, c_ptr + 1, not a_bool)

    helper(0, 0, 0, True)
    return all


if __name__ == "__main__":

    s = "a!!!b.c.d,e'f,ghi"
    assert reverse_ignore_special(s) == "i!!!h.g.f,e'd,cba"

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

    arr = [5, 1, 3, 4, 7]
    assert count_triplets_smaller_sum(arr, 12) == 4

    arr = [4, 3, 7, 8, 6, 2, 1]
    convert_zig_zag(arr)
    assert arr == [4, 7, 3, 8, 2, 6, 1]

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
