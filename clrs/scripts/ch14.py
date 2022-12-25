"""Contain implementation for ch14."""
from typing import List, Tuple

PRICES = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
REVENUE = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

MATRIX_SIZE = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
OPERATIONS = [0, 15750, 7875, 9375, 11875, 15125]

X = "ABCBDAB"
Y = "BDCABA"

P = [0.00, 0.15, 0.10, 0.05, 0.10, 0.20]
Q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]


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
    """Compute minimal operations in matrix multiplication bottom_up.

    Args:
        p (List[Tuple[int, int]]): list of matrix sizes.
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


def recursive_matrix_chain(p: List[Tuple[int, int]], i: int, j: int) -> int:
    """Compute minimal operations in matrix multiplication recursively.

    Args:
        p (List[Tuple[int, int]]): list of matrix sizes.
        i (int): start.
        j (int): end.

    Returns:
        int: minimum operations.
    """
    if i == j:
        return 0

    m = [[float("inf")] * (j + 1) for _ in range(i + 1)]

    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k)
        q += recursive_matrix_chain(p, k + 1, j)
        q += p[i][0] * p[k][1] * p[j][1]

        if q < m[i][j]:
            m[i][j] = q

    return m[i][j]


def memoized_matrix_chain(p: List[Tuple[int, int]], n: int) -> int:
    """Compute minimal operations in matrix multiplication top-down.

    Args:
        p (List[Tuple[int, int]]): list of matrix sizes.
        n (int): number of matrices

    Returns:
        int: minimum operations.
    """
    m = [[float("inf")] * (n) for _ in range(n)]
    return lookup_chain(m, p, 0, n - 1)


def lookup_chain(m: List[List[int]], p: List[Tuple[int, int]], i: int, j: int) -> int:
    """_Compute minimal operations in matrix multiplication top-down with memoization.

    Args:
        m (List[List[int]]): memo.
        p (List[Tuple[int, int]]): list of matrix sizes.
        i (int): start.
        j (int): end.

    Returns:
        int: minimum operations.
    """
    if m[i][j] < float("inf"):
        return m[i][j]

    if i == j:
        m[i][j] = 0

    else:
        for k in range(i, j):

            q = lookup_chain(m, p, i, k)
            q += lookup_chain(m, p, k + 1, j)
            q += p[i][0] * p[k][1] * p[j][1]

            if q < m[i][j]:
                m[i][j] = q

    return m[i][j]


def lcs_length(X: str, Y: str, m: int, n: int) -> Tuple[List[List[int]], List[List]]:
    """Find length of LCS of two sequences.

    Args:
        X (str): first sequence.
        Y (str): second sequence.
        m (int): length of first sequence.
        n (int): length of second sequence.

    Returns:
        Tuple[List[List[int]], List[List]]: memo and path.
    """
    b = [[0] * (n + 1) for _ in range(m + 1)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = (-1, -1)

            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = (-1, 0)

            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = (0, -1)

    return c, b


def print_lcs(b: List[List], X: str, i: int, j: int) -> None:
    """Print LCS.

    Args:
        b (List[List]): path.
        X (str): first sequence.
        i (int): index of first sequence.
        j (int): index of second sequence.
    """
    if i == 0 or j == 0:
        return
    if b[i][j] == (-1, -1):
        print_lcs(b, X, i - 1, j - 1)
        print(X[i - 1])

    elif b[i][j] == (-1, 0):
        print_lcs(b, X, i - 1, j)

    else:
        print_lcs(b, X, i, j - 1)


def optimal_bst(p: List, q: List, n: int) -> Tuple[List[List], List[List]]:
    """Find optimal bst.

    Args:
        p (List): probabilities of keys.
        q (List): probabilities of dummies.
        n (int): number of nodes.

    Returns:
        Tuple[List[List], List[List]]: cost matrix and root matrix.
    """
    e = [[0] * (n + 1) for _ in range(n + 2)]
    w = [[0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for gap in range(1, n + 1):

        for i in range(1, n - gap + 2):
            j = i + gap - 1
            e[i][j] = float("inf")
            w[i][j] = w[i][j - 1] + p[j] + q[j]

            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root


def optimal_bst2(p: List, q: List, n: int) -> Tuple[List[List], List[List]]:
    """Find optimal bst with zero index.

    Args:
        p (List): probabilities of keys.
        q (List): probabilities of dummies.
        n (int): number of nodes.

    Returns:
        Tuple[List[List], List[List]]: cost matrix and root matrix.
    """
    e = [[0] * (n + 1) for _ in range(n + 1)]
    w = [[0] * (n + 1) for _ in range(n + 1)]
    root = [[0] * (n) for _ in range(n)]

    for i in range(1, n + 2):
        e[i - 1][i - 1] = q[i - 1]
        w[i - 1][i - 1] = q[i - 1]

    for gap in range(1, n + 1):

        for i in range(1, n - gap + 2):
            j = i + gap - 1
            e[i - 1][j] = float("inf")
            w[i - 1][j] = w[i - 1][j - 1] + p[j] + q[j]

            for r in range(i, j + 1):
                t = e[i - 1][r - 1] + e[r][j] + w[i - 1][j]
                if t < e[i - 1][j]:
                    e[i - 1][j] = t
                    root[i - 1][j - 1] = r

    return e, root


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
        assert p[0][-1] == OPERATIONS[i - 1]

        print("Operations: ")
        print(p[0][-1])
        print("Parens: ")
        print(print_optimal_parens(s, 0, i - 1))

        p = recursive_matrix_chain(MATRIX_SIZE, 0, i - 1)
        assert p == OPERATIONS[i - 1]
        print("Operations: ")
        print(p)

        p = memoized_matrix_chain(MATRIX_SIZE, i)
        assert p == OPERATIONS[i - 1]
        print("Operations: ")
        print(p)

    # 14.4 Longest common subsequence

    c, b = lcs_length(X, Y, len(X), len(Y))
    assert c[-1][-1] == 4
    print_lcs(b, X, len(X), len(Y))

    # 14.5 Optimal binasry search tree

    e, root = optimal_bst(P, Q, len(P) - 1)
    assert e[1][-1] == 2.75
    assert root[1][-1] == 2

    e, root = optimal_bst2(P, Q, len(P) - 1)
    assert e[0][-1] == 2.75
    assert root[0][-1] == 2
