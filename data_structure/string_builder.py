"""Implement StringBuilder."""
# https://gist.github.com/MohamedHajr/d7cee6a9aeaf01e0d7915eb44f7d8e6d

from __future__ import absolute_import, print_function


class StringBuilder:
    """Create StringBuilder Class."""

    def __init__(self) -> None:
        """Initialize Class."""
        self.array = []

    def append(self, s: str) -> None:
        """Add string to list.

        Args:
            s (str): string to be added.
        """
        self.array.append(s)

    def __str__(self) -> str:
        """Convert array to string.

        Returns:
            str: converted string.
        """
        return "".join(self.array)
