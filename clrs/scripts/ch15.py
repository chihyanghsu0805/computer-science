"""Contain implementation for ch15."""
from typing import List

START = [0, 1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
END = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]


def recursive_activity_selector(s: List, f: List, k: int, n: int) -> List:
    """Solve maximum activity selection recursively.

    Args:
        s (List): list of start times.
        f (List): list of finish times.
        k (int): start index.
        n (int): number of activities.

    Returns:
        List: list with activity indices.
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1

    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)

    else:
        return []


def greedy_activity_selector(s: List, f: List, n: int) -> List:
    """Solve maximum activity selection greedy.

    Args:
        s (List): list of start times.
        f (List): list of finish times.
        n (int): number of activities.

    Returns:
        List: list with activity indices.
    """
    A = [1]
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A = A + [m]
            k = m

    return A


if __name__ == "__main__":

    a = recursive_activity_selector(START, END, 0, len(START) - 1)
    print(a)
    a = greedy_activity_selector(START, END, len(START) - 1)
    print(a)
