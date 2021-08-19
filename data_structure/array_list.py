"""Implement ArrayList."""
# https://code.luasoftware.com/tutorials/coding-interview/implement-dynamic-array-in-python/

from __future__ import absolute_import, print_function

from numbers import Number


class ArrayList:
    """Implement ArrayList."""

    def __init__(self, size: int = 2) -> None:
        """Initialize Class.

        Args:
            size (int, optional): array size. Defaults to 10.
        """
        self.max_size = size
        self.array = [None] * size
        self.current_size = 0

    def add(self, value: Number) -> None:
        """Add number to array.

        Args:
            value (Number): input number.
        """
        if self.current_size >= self.max_size:
            self._increase_size()

        self.array[self.current_size] = value
        self.current_size += 1

    def _increase_size(self) -> None:
        """Increase array size and copy numbers to bigger array."""
        self.max_size *= 2
        new_array = [None] * self.max_size
        for idx, value in enumerate(self.array):
            new_array[idx] = value
        self.array = new_array

    def get(self, index: int) -> Number:
        """Get number in array by index.

        Args:
            index (int): index in array.

        Returns:
            Number: value at index.
        """
        assert index > 0 and index < self.max_size
        return self.array[index]

    def delete(self, index: int) -> None:
        """Delete index from array.

        Args:
            index (int): index in array.
        """
        assert index > 0 and index < self.max_size
        for i in range(index, self.current_size):
            self.array[i] = self.array[i + 1]

        self.current_size -= 1
