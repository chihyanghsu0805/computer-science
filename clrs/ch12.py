"""Contain implementation for chapter 12."""

from data_structures import BinarySearchTree, BinarySearchTreeNode


def inorder_tree_walk(x: BinarySearchTreeNode) -> None:
    """Traverse tree inorder.

    Args:
        x (BinarySearchTreeNode): node.
    """
    if not x:
        return

    inorder_tree_walk(x.left)
    print(x.key)
    inorder_tree_walk(x.right)


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.tree_insert(BinarySearchTreeNode(2))
    bst.tree_insert(BinarySearchTreeNode(1))
    bst.tree_insert(BinarySearchTreeNode(3))

    inorder_tree_walk(bst.root)
