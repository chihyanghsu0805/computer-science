"""Test Bit Algorithms."""

from algorithms.bit import (
    Trie,
    find_magic_n,
    find_max_subarray_xor,
    find_once,
    sum_bit_differences,
    swap_bits,
)


def test_find_max_subarray_xor():
    """Test Find Max Subarray XOR."""
    arr = [8, 1, 2, 12]
    trie = Trie()
    assert find_max_subarray_xor(trie, arr) == 15


def test_find_magic_n():
    """Test Find Magic N."""
    assert find_magic_n(5) == 130


def test_sum_bit_differences():
    """Test Sum Bit Differences."""
    arr = [1, 3, 5]
    assert sum_bit_differences(arr) == 8


def test_swap_bits():
    """Test Swap Bits."""
    assert swap_bits(23) == 43


def test_find_once():
    """Test Find Once."""
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
    assert find_once(arr) == 7
