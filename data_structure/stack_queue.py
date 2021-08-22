"""Implement Stack and Queue."""

from __future__ import absolute_import, print_function

from numbers import Number


class Stack:
    """Create Stack Class."""

    def __init__(self) -> None:
        """Initialize Class."""
        self.arr = []

    def push(self, value: Number) -> None:
        """Push value to top of stack.

        Args:
            value (Number): input value.
        """
        self.arr.append(value)

    def pop(self) -> None:
        """Pop value from top."""
        self.arr.pop()

    def top(self) -> Number:
        """Return value from top of stack.

        Raises:
            IndexError: Empty list.

        Returns:
            Number: value from top.
        """
        if not self.arr:
            raise IndexError
        return self.arr[-1]

    def is_empty(self) -> bool:
        """Check whether stack is empty.

        Returns:
            bool: True if stack is empty.
        """
        return len(self.arr) == 0
