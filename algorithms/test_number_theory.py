"""Test Algorithms for Number Theory."""

from algorithms.number_theory import (
    check_primality,
    check_primality2,
    count_euler_totient,
    count_euler_totient2,
    count_primes,
    modular_exponent,
    modular_multiplicative_inverse,
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
