"""Implement Trie."""

from __future__ import absolute_import, print_function


class Trie:
    """Create Trie Class."""

    def __init__(self) -> None:
        """Initialize class."""
        self.trie = {}

    def insert(self, word: str) -> None:
        """Insert word into trie.

        Args:
            word (str): word to be inserted.
        """
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["#"] = True

    def search(self, word: str) -> bool:
        """Search word in trie.

        Args:
            word (str): word to be searched.

        Returns:
            bool: whether word is in trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]

        return "#" in t

    def starts_with(self, word: str) -> bool:
        """Search prefix in trie.

        Args:
            word (str): prefix to be searched.

        Returns:
            bool: whether predix is in trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return True
