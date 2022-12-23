"""Contain implementation for ch14."""
from typing import List, Tuple

PRICES = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
REVENUE = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]


def cut_rod(p: List, n: int) -> int:
    """Cut rod recursively.

    Args:
        p (List): prices.
        n (int): length.

    Returns:
        int: revenue
    """
    if n == 0:
        return 0

    q = -float("inf")

    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))

    return q


def memoized_cut_rod(p: List, n: int) -> int:
    """Cut rod with memo.

    Args:
        p (List): prices.
        n (int): length.

    Returns:
        int: revenue
    """
    r = [-float("inf")] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: List, n: int, r: List) -> int:
    """Cut rod with memo.

    Args:
        p (List): prices.
        n (int): length.
        r (List): memo.

    Returns:
        int: revenue
    """
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0

    else:
        q = -float("inf")
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))

    r[n] = q
    return q


def bottom_up_cut_rod(p: List, n: int) -> int:
    """Cut rod bottom up.

    Args:
        p (List): prices.
        n (int): length.

    Returns:
        int: revenue
    """
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])

        r[j] = q

    return r[n]


def extend_bottom_up_cut_rod(p: List, n: int) -> Tuple[List, List]:
    """Cut rod bottom up with solution.

    Args:
        p (List): price.
        n (int): length

    Returns:
        Tuple[List, List]: revenue, solution
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)

    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(j):
            if q < p[i] + r[j - i - 1]:
                q = p[i] + r[j - i - 1]
                s[j] = i + 1

        r[j] = q

    return r, s


def print_cut_rod_solution(p: List, n: int) -> None:
    """Print solution.

    Args:
        p (List): price.
        n (int): length.
    """
    r, s = extend_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


if __name__ == "__main__":

    # 14.1 Cut rod

    for i in range(1, len(PRICES) + 1):
        r = cut_rod(PRICES, i)
        assert r == REVENUE[i - 1]
        r = memoized_cut_rod(PRICES, i)
        assert r == REVENUE[i - 1]
        r = bottom_up_cut_rod(PRICES, i)
        assert r == REVENUE[i - 1]
        print("Cuts: ")
        print_cut_rod_solution(PRICES, i)
        print("Revenue: ")
        print(r)
