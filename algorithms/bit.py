"""Algorithms for Bit Manipulation."""
from __future__ import absolute_import, print_function

from typing import List


class Node:
    """Constructor."""

    def __init__(self, value: int) -> None:
        """Initialize Class.

        Args:
            value (int): value.
        """
        self.value = value
        self.lt = None  # 0
        self.rt = None  # 1


class Trie:
    """Constructor."""

    def __init__(self):
        """Initialize Class."""
        self.root = Node(0)

    def insert(self, pre_xor: int) -> None:
        """Insert value into Trie.

        Args:
            pre_xor (int): value.
        """
        self.temp = self.root
        for i in range(31, -1, -1):
            value = pre_xor & (1 << i)
            if value:
                if not self.temp.rt:
                    self.temp.rt = Node(0)
                self.temp = self.temp.rt
            if not value:
                if not self.temp.lt:
                    self.temp.lt = Node(0)
                self.temp = self.temp.lt

        self.temp.value = pre_xor

    def query(self, xor: int) -> int:
        """Query trie for value.

        Args:
            xor (int): value.

        Returns:
            int: result.
        """
        self.temp = self.root
        for i in range(31, -1, -1):

            value = xor & (1 << i)

            if value:
                if self.temp.lt:
                    self.temp = self.temp.lt
                elif self.temp.rt:
                    self.temp = self.temp.rt
            else:
                if self.temp.rt:
                    self.temp = self.temp.rt
                elif self.temp.lt:
                    self.temp = self.temp.lt
        return xor ^ self.temp.value


def find_max_subarray_xor(t: Trie, arr: List) -> int:
    """Find Maximum XOR Subarray.

    Args:
        t (Trie): Trie with values and bits.
        arr (List): array with value.

    Returns:
        int: maxium XOR.
    """
    t.insert(0)
    result = -float("inf")
    pre_xor = 0

    for n in arr:
        pre_xor = pre_xor ^ n
        t.insert(pre_xor)

        result = max(result, t.query(pre_xor))

    return result


def find_magic_n(n: int) -> int:
    """Find Nth Magic Number.

    Args:
        n (int): n.

    Returns:
        int: Nth magic Number.
    """
    # Magic number is power of 5 or sum of power of 5.

    power = 1
    answer = 0

    while n:
        power = power * 5

        if n & 1:
            answer += power

        n >>= 1

    return answer


def sum_bit_differences(arr: List) -> int:
    """Sum of Bit Differences.

    Args:
        arr (List): array of numbers.

    Returns:
        int: Sum.
    """
    answer = 0
    N = len(arr)

    for i in range(32):

        count = 0
        for n in arr:
            if n & (1 << i):
                count += 1

        answer += count * (N - count) * 2

    return answer


def swap_bits(x: int) -> int:
    """Swap Bits.

    Args:
        x (int): given number.

    Returns:
        int: swapped number.
    """
    even_bits = x & 0xAAAAAAAA
    odd_bits = x & 0x55555555

    even_bits >>= 1
    odd_bits <<= 1

    return even_bits | odd_bits


def find_once(arr: List) -> int:
    """Find Element that Appears Only Once.

    Args:
        arr (List): array of numbers.

    Returns:
        int: number only once.
    """
    result = 0

    for i in range(32):

        _sum = 0
        x = 1 << i
        for n in arr:
            if n & x:
                _sum += 1

        if _sum % 3 != 0:
            result = result | x

    return result


if __name__ == "__main__":

    arr = [8, 1, 2, 12]
    trie = Trie()
    assert find_max_subarray_xor(trie, arr) == 15

    assert find_magic_n(5) == 130

    arr = [1, 3, 5]
    assert sum_bit_differences(arr) == 8

    assert swap_bits(23) == 43

    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
    assert find_once(arr) == 7
