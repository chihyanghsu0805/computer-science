"""Implement BinaryTree."""

from __future__ import absolute_import, print_function

from typing import List


class BinaryTree:
    """Create BinaryTree Class."""

    def __init__(self, value: int = None) -> None:
        """Initialize Class.

        Args:
            value (int, optional): [description]. Defaults to None.
        """
        self.value = value
        self.lt = None
        self.rt = None

    def traverse_inorder(self) -> List:
        """Traverse the tree by inorder (lt, Root, rt).

        Args:
            arr (List, optional): array to store values. Defaults to [].

        Returns:
            List: updated array.
        """
        lt = self.lt.traverse_inorder() if self.lt else []
        rt = self.rt.traverse_inorder() if self.rt else []
        return lt + [self.value] + rt

    def traverse_preorder(self) -> List:
        """Traverse the tree by preorder (Root, lt, rt)."""
        lt = self.lt.traverse_preorder() if self.lt else []
        rt = self.rt.traverse_preorder() if self.rt else []
        return [self.value] + lt + rt

    def traverse_postorder(self) -> None:
        """Traverse the tree by preorder (lt, rt, Root)."""
        lt = self.lt.traverse_postorder() if self.lt else []
        rt = self.rt.traverse_postorder() if self.rt else []
        return lt + rt + [self.value]
