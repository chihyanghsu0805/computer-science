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


def represent_binary(n: int) -> str:
    """Represent Number in Binary.

    Args:
        n (int): given number.

    Returns:
        str: binary string.
    """
    s = ""

    for i in range(32):

        bit = 1 << i

        if n & bit:
            s = "1" + s
        else:
            s = "0" + s

    return s


def represent_binary2(n: int) -> str:
    """Represent Number in Binary.

    Args:
        n (int): given number.

    Returns:
        str: binary string.
    """
    s = ""
    mask = 0xFFFFFFFF

    for i in range(32):

        bit = 1 << i

        if n & bit:
            s = "1" + s
        else:
            s = "0" + s

        mask = mask << 1
        if not n & mask:
            break

    return s


def count_all_bits(n: int) -> int:
    """Count All Bits till N.

    Args:
        n (int): given number.

    Returns:
        int: number of bits.
    """
    bits = 0
    memo = [0] * (n + 1)

    for i in range(1, n + 1):
        memo[i] = memo[i // 2]
        if i % 2 == 1:
            memo[i] += 1

        bits += memo[i]

    return bits


def rotate_bits(n: int, k: int) -> int:
    """Rotate Bits.

    Args:
        n (int): given number.
        k (int): number of rotations.

    Returns:
        int: rotated number.
    """

    def rotate_left(n: int, k: int):
        return ((n << k) & 0xFFFFFFFF) | (n >> (32 - k))

    def rotate_right(n: int, k: int):
        return (n >> k) | ((n << (32 - k)) & 0xFFFFFFFF)

    return rotate_left(n, k), rotate_right(n, k)


def count_flip_bits(a: int, b: int) -> int:
    """Count Number of Bits to flip so a == b.

    Args:
        a (int): first number.
        b (int): second number.

    Returns:
        int: number of bits.
    """
    xor = a ^ b
    count = 0
    while xor:
        if xor & 1:
            count += 1

        xor >>= 1

    return count


def find_next_sparse(n: int) -> int:
    """Find Next Sparse Number, no consecutive 11s.

    Args:
        n (int): given number.

    Returns:
        int: next sparse number.
    """
    binary = []
    while n:
        binary.append(n & 1)
        n >>= 1
    binary.append(0)
    N = len(binary)

    last_final = 0

    for i in range(1, N - 1):

        if binary[i] and binary[i - 1] and not binary[i + 1]:

            binary[i + 1] = 1

            for j in range(i, last_final - 1, -1):
                binary[j] = 0

            last_final = i + 1

    ans = 0
    for i in range(N):
        ans += binary[i] * (1 << i)

    return ans


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

    assert represent_binary(7) == "00000000000000000000000000000111"
    assert represent_binary(4) == "00000000000000000000000000000100"
    assert represent_binary2(7) == "111"
    assert represent_binary2(4) == "100"

    assert count_all_bits(8) == 13
    assert count_all_bits(3) == 4
    assert count_all_bits(6) == 9
    assert count_all_bits(7) == 12

    assert rotate_bits(16, 2)[0] == 64
    assert rotate_bits(16, 2)[1] == 4

    assert count_flip_bits(10, 20) == 4

    assert find_next_sparse(38) == 40
