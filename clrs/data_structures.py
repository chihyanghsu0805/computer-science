"""Contain data structures."""

__all__ = ["BinarySearchTree", "BinarySearchTreeNode"]


class BinarySearchTreeNode:
    """Class for instance of binary search tree node."""

    def __init__(self, key: any, satellite: any) -> None:
        """Initialize class.

        Args:
            key (any): key for node.
            satellite (any): satellite for node.
        """
        self.key = key
        self.satellite = satellite
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class for instance of binary search tree."""

    def __init__(self) -> None:
        """Initialize class."""
        self.root = None

    def tree_insert(self, z: BinarySearchTreeNode) -> None:
        """Insert node into tree.

        Args:
            z (BinarySearchTreeNode): node to be inserted.
        """
        x = self.root
        y = None
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z

        elif z.key < y.key:
            y.left = z

        else:
            y.right = z
