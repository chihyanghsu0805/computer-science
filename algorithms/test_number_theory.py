"""Test Algorithms for Number Theory."""

from algorithms.number_theory import (
    Point,
    check_primality,
    check_primality2,
    compute_convex_hull,
    count_euler_totient,
    count_euler_totient2,
    count_primes,
    find_x_remainder,
    greatest_common_divisor,
    greatest_common_divisor_coefficients,
    lucas_theorem,
    modular_exponent,
    modular_multiplicative_inverse,
    nCrModp,
    segmented_sieve,
)


def test_modular_exponent():
    """Test Modular Exponent."""
    assert modular_exponent(2, 5, 13) == 6


def test_modular_multiplicative_inverse():
    """Test Modular Multiplicative Inverse."""
    assert modular_multiplicative_inverse(3, 11) == 4


def test_check_primality():
    """Test Check Primality."""
    assert check_primality(13)
    assert not check_primality(33)
    assert check_primality2(13)
    assert not check_primality2(33)


def test_count_euler_totient():
    """Test Count Euler Totient."""
    res = [count_euler_totient(n) for n in range(1, 11)]
    assert res == [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    res = [count_euler_totient2(n) for n in range(1, 11)]
    assert res == [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]


def test_count_primes():
    """Test Count Primes."""
    assert count_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_compute_convex_hull():
    """Test Compute Convex Hull."""
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


def test_euclidean_algorithm():
    """Test Euclidean Algorithm."""
    assert greatest_common_divisor(10, 15) == 5
    assert greatest_common_divisor(10, 35) == 5
    assert greatest_common_divisor(2, 31) == 1

    assert greatest_common_divisor_coefficients(10, 15) == (5, -1, 1)
    assert greatest_common_divisor_coefficients(10, 35) == (5, -3, 1)
    assert greatest_common_divisor_coefficients(2, 31) == (1, -15, 1)


def test_segmented_sieve():
    """Test Segmented Sieve."""
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


def test_find_x_remainder():
    """Test Find X Remainder."""
    numbers = [3, 4, 5]
    remains = [2, 3, 1]
    assert find_x_remainder(numbers, remains) == 11


def test_nCrModp():
    """Test nCrModp."""
    n = 1000
    r = 900
    p = 13
    assert nCrModp(n, r, p) == 8
    assert lucas_theorem(n, r, p) == 8
