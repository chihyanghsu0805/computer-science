"""Algorithms for Number Theory."""
from __future__ import absolute_import, print_function

import math
import random
from typing import List


class Point:
    """Constructor."""

    def __init__(self, x: int, y: int):
        """Initialize Class.

        Args:
            x (int): x coordinate.
            y (int): y coordinate.
        """
        self.x = x
        self.y = y


def modular_exponent(x: int, y: int, p: int) -> int:
    """Modular Exponent.

    Args:
        x (int): base.
        y (int): power.
        p (int): modulo.

    Returns:
        int: result.
    """
    # (ab) % p = ((a%p)*(b%p))%p
    res = 1

    x = x % p
    if not x:
        return 0

    while y > 0:

        if y & 1 == 1:
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p
    return res


def check_primality(n: int) -> bool:
    """Check N is Prime.

    Args:
        n (int): given integer.

    Returns:
        bool: True if n is Prime.
    """
    if n <= 1:
        return False

    sqrt_n = int(n ** (1 / 2))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True


def check_primality2(n: int, k: int = 3) -> bool:
    """Check N is Prime.

    Args:
        n (int): given integer.

    Returns:
        bool: True if n is Prime.
    """
    # if n is prime: a^(n-1) % n =1, Fermat's Theorem
    # higher k indicates probability of correct

    if n == 1 or n == 4:
        return False

    if n == 2 or n == 3:
        return True

    for i in range(k):
        a = random.randint(2, n - 2)
        if modular_exponent(a, n - 1, n) != 1:
            return False
    return True


def modular_multiplicative_inverse(a: int, m: int) -> int:
    """Modular Multiplicative Inverse.

    Args:
        a (int): base.
        m (int): modulo.

    Returns:
        int: solution.
    """
    # (a*x) % m == 1
    for x in range(1, m):

        if ((a % m) * (x % m)) % m == 1:
            return x

    return -1


def greatest_common_divisor(a: int, b: int) -> int:
    """Find Greatest Common Divisor.

    Args:
        a (int): first number.
        b (int): second number.

    Returns:
        int: gcd.
    """
    if not a:
        return b
    return greatest_common_divisor(b % a, a)


def count_euler_totient(n: int) -> int:
    """Count Euler's Totient.

    Args:
        n (int): given number.

    Returns:
        int: Euler's Totient
    """
    result = 1
    for i in range(2, n):
        if greatest_common_divisor(n, i) == 1:
            result += 1

    return result


def count_euler_totient2(n: int) -> int:
    """Count Euler's Totient.

    Args:
        n (int): given number.

    Returns:
        int: Euler's Totient
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p += 1

    if n > 1:
        result = result * (1.0 - (1.0 / float(n)))
    return int(result)


def count_primes(n: int) -> int:
    """Count Primes till N.

    Args:
        n (int): Given number.

    Returns:
        int: number of primes.
    """
    prime_bool = [True] * (n + 1)
    p = 2
    # use while to compute p*p instead of sqrt.
    while p * p <= n:

        if prime_bool[p]:

            for j in range(p * p, n + 1, p):
                prime_bool[j] = False

        p += 1

    primes = [i for i in range(2, n + 1) if prime_bool[i]]
    return primes


def compute_convex_hull(points: List) -> List:
    """Compute Convex  Hull.

    Args:
        points (List): List of points.

    Returns:
        List: List of convex hull points.
    """
    N = len(points)
    if N < 3:
        return

    def find_lt_most(points):
        lt_most = 0

        for i in range(1, N):
            if points[i].x < points[lt_most].x:
                lt_most = i
            elif points[i].x == points[lt_most].x:
                if points[i].y > points[lt_most].y:
                    lt_most = i

        return lt_most

    def compute_orientation(a, b, c):
        value = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)

        if value == 0:
            return 0

        elif value > 0:
            return 1
        else:
            return 2

    lt = find_lt_most(points)

    hull = []
    p = lt
    q = 0

    while True:

        hull.append(p)

        q = (p + 1) % N

        for i in range(N):
            if compute_orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == lt:
            break

    convex_hull = [(points[i].x, points[i].y) for i in hull]

    return convex_hull


def greatest_common_divisor_coefficients(a: int, b: int) -> List:
    """Find Greatest Common Divisor with coefficients such that ax+by = 1.

    Args:
        a (int): first number.
        b (int): second number.

    Returns:
        int: gcd, x, y.
    """
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = greatest_common_divisor_coefficients(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def segmented_sieve(n: int) -> List:
    """Count Primes till N in Smaller Segments.

    Args:
        n (int): given number.

    Returns:
        List: primes.
    """
    temp = []
    limit = int(math.floor(math.sqrt(n)) + 1)
    primes = count_primes(limit)

    lo = limit
    hi = limit * 2

    while lo < n:

        if hi >= n:
            hi = n

        bool_prime = [True for i in range(limit + 1)]

        for i in range(len(primes)):

            lo_limit = lo // primes[i] * primes[i]

            if lo_limit < lo:
                lo_limit += primes[i]

            for j in range(lo_limit, hi, primes[i]):
                bool_prime[j - lo] = False

        for i in range(lo, hi):
            if bool_prime[i - lo]:
                temp.append(i)

        lo = lo + limit
        hi = hi + limit

    return primes + temp


def find_x_remainder(numbers: List, remains: List) -> int:
    """Find X with Remainder.

    Args:
        numbers (List): list of numbers.
        remains (List): list of remains.

    Returns:
        int: solution.
    """
    N = len(numbers)

    x = 1

    while True:

        j = 0

        while j < N:

            if x % numbers[j] != remains[j]:
                break

            j += 1

        if j == N:
            return x

        x += 1


def nCrModp(n: int, r: int, p: int) -> int:
    """Compute nCrModp.

    Args:
        n (int): n.
        r (int): r.
        p (int): p.

    Returns:
        int: result.
    """
    if r > n - r:
        r = n - r
    C = [0 for i in range(r + 1)]
    C[0] = 1

    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j - 1]) % p

    return C[r]


def lucas_theorem(n: int, r: int, p: int) -> int:
    """Compute nCrModp.

    Args:
        n (int): n.
        r (int): r.
        p (int): p.

    Returns:
        int: result.
    """
    # nCr % p

    if not r:
        return 1

    ni = n % p
    ri = r % p

    return (lucas_theorem(n // p, r // p, p) * nCrModp(ni, ri, p)) % p


if __name__ == "__main__":

    assert modular_exponent(2, 5, 13) == 6
    assert modular_multiplicative_inverse(3, 11) == 4
    assert check_primality(13)
    assert not check_primality(33)
    assert check_primality2(13)
    assert not check_primality2(33)

    res = [count_euler_totient(n) for n in range(1, 11)]
    assert res == [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    res = [count_euler_totient2(n) for n in range(1, 11)]
    assert res == [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    assert count_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    points = []
    points.append(Point(0, 3))
    points.append(Point(2, 2))
    points.append(Point(1, 1))
    points.append(Point(2, 1))
    points.append(Point(3, 0))
    points.append(Point(0, 0))
    points.append(Point(3, 3))

    convex_hull = compute_convex_hull(points)
    assert convex_hull == [(0, 3), (0, 0), (3, 0), (3, 3)]

    assert greatest_common_divisor(10, 15) == 5
    assert greatest_common_divisor(10, 35) == 5
    assert greatest_common_divisor(2, 31) == 1

    assert greatest_common_divisor_coefficients(10, 15) == (5, -1, 1)
    assert greatest_common_divisor_coefficients(10, 35) == (5, -3, 1)
    assert greatest_common_divisor_coefficients(2, 31) == (1, -15, 1)

    assert segmented_sieve(100) == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]

    numbers = [3, 4, 5]
    remains = [2, 3, 1]
    assert find_x_remainder(numbers, remains) == 11

    n = 1000
    r = 900
    p = 13
    assert nCrModp(n, r, p) == 8
    assert lucas_theorem(n, r, p) == 8
