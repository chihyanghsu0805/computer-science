"""Contain implementation for ch14."""
from typing import List, Tuple

PRICES = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
REVENUE = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

MATRIX_SIZE = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
OPERATIONS = [0, 15750, 7875, 9375, 11875, 15125]


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


def matrix_chain_order(p: List[Tuple], n: int) -> Tuple[List[List], List[List]]:
    """Compute optimal parentheses for minimal operations in matrix multiplication.

    Args:
        p (List[Tuple]): list of matrix sizes.
        n (int): number of matrices.

    Returns:
        Tuple[List[List], List[List]]: 2d array of operations and parentheses.
    """
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = 0

    for gap in range(2, n + 1):

        for i in range(n - gap + 1):

            j = i + gap - 1

            m[i][j] = float("inf")

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j]
                q += p[i][0] * p[k][1] * p[j][1]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parens(s: List[List], i: int, j: int) -> str:
    """Print optimal parentheses.

    Args:
        s (List[List]): 2d array of parenthese.
        i (int): start.
        j (int): end.

    Returns:
        str: string with matrix indices to parenthesize.
    """
    if i == j:
        return f"A_{i}"
    else:
        ij = print_optimal_parens(s, i, s[i][j])
        jk = print_optimal_parens(s, s[i][j] + 1, j)
        return f"({ij}x{jk})"


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

    # 14.2 Matrix chain multiplication

    for i in range(1, len(MATRIX_SIZE) + 1):
        p, s = matrix_chain_order(MATRIX_SIZE, i)
        print(s)
        assert p[0][-1] == OPERATIONS[i - 1]
        print("Operations: ")
        print(p[0][-1])
        print("Parens: ")
        print(print_optimal_parens(s, 0, i - 1))
