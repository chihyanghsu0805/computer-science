"""Contain binary tree."""

__all__ = ["BinaryTree", "BinaryTreeNode"]


class BinaryTreeNode:
    """Class for instance of binary tree node."""

    def __init__(self, key: any, satellite: any = None) -> None:
        """Initialize class.

        Args:
            key (any): key for node.
            satellite (any, optional): satellite for node. Defaults to None.
        """
        self.key = key
        self.satellite = satellite
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    """Class for instance of binary tree."""

    # compute_height
    # tree_search
    # tree_minimum
    # tree_maximum
    # tree_insert
    # tree_delete
    pass
