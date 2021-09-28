"""Algorithms for Number Theory."""
from __future__ import absolute_import, print_function

import random


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
