"""Test Bit Algorithms."""

from algorithms.bit import (
    Trie,
    count_all_bits,
    count_flip_bits,
    find_magic_n,
    find_max_subarray_xor,
    find_next_sparse,
    find_once,
    represent_binary,
    represent_binary2,
    rotate_bits,
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


def test_represent_binary():
    """Test Represent Binary."""
    assert represent_binary(7) == "00000000000000000000000000000111"
    assert represent_binary(4) == "00000000000000000000000000000100"
    assert represent_binary2(7) == "111"
    assert represent_binary2(4) == "100"


def test_count_all_bits():
    """Test Count All Bits."""
    assert count_all_bits(8) == 13
    assert count_all_bits(3) == 4
    assert count_all_bits(6) == 9
    assert count_all_bits(7) == 12


def test_rotate_bits():
    """Teset Rotate Bits."""
    assert rotate_bits(16, 2)[0] == 64
    assert rotate_bits(16, 2)[1] == 4


def test_count_flip_bits():
    """Test Count Flip Bits."""
    assert count_flip_bits(10, 20) == 4


def test_find_next_sparse():
    """Test Find Next Sparse."""
    assert find_next_sparse(38) == 40
