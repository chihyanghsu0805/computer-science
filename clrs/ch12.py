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

    bstnode_1 = BinarySearchTreeNode(1)
    bstnode_2 = BinarySearchTreeNode(2)
    bstnode_3 = BinarySearchTreeNode(3)

    # Tree insertion
    bst1 = BinarySearchTree()
    bst1.tree_insert(bstnode_2)
    bst1.tree_insert(bstnode_1)
    bst1.tree_insert(bstnode_3)

    # Inorder
    print("Inorder traversal of Binary Search Tree gives sorted keys:")
    inorder_tree_walk(bst1.root)

    # Tree search
    node = bst1.tree_search(bstnode_1.key)
    assert node.key == bstnode_1.key
    print(f"Node with key = {bstnode_1.key} found.")

    key = 4
    node = bst1.tree_search(key)
    assert node is None
    print(f"Node with key = {key} not found.")

    # Tree minimum
    node = bst1.tree_minimum(bstnode_1)
    assert node.key == 1
    print(f"Tree minimum rooted at {bstnode_1.key} is: {node.key}.")

    node = bst1.tree_minimum(bstnode_2)
    assert node.key == 1
    print(f"Tree minimum rooted at {bstnode_2.key} is: {node.key}.")

    node = bst1.tree_minimum(bstnode_3)
    assert node.key == 3
    print(f"Tree minimum rooted at {bstnode_3.key} is: {node.key}.")

    # Tree maximum
    node = bst1.tree_maximum(bstnode_1)
    assert node.key == 1
    print(f"Tree maximum rooted at {bstnode_1.key} is: {node.key}.")

    node = bst1.tree_maximum(bstnode_2)
    assert node.key == 3
    print(f"Tree maximum rooted at {bstnode_2.key} is: {node.key}.")

    node = bst1.tree_maximum(bstnode_3)
    assert node.key == 3
    print(f"Tree maximum rooted at {bstnode_3.key} is: {node.key}.")

    # Tree successor
    node = bst1.tree_successor(bstnode_1)
    assert node.key == 2
    print(f"Tree successor of {bstnode_1.key} is: {node.key}.")

    node = bst1.tree_successor(bstnode_2)
    assert node.key == 3
    print(f"Tree successor of {bstnode_2.key} is: {node.key}.")

    node = bst1.tree_successor(bstnode_3)
    assert node is None
    print(f"Tree successor of {bstnode_3.key} does not exist.")

    # Tree predecessor
    node = bst1.tree_predecessor(bstnode_1)
    assert node is None
    print(f"Tree predecessor of {bstnode_1.key} does not exist.")

    node = bst1.tree_predecessor(bstnode_2)
    assert node.key == 1
    print(f"Tree predecessor of {bstnode_2.key} is: {node.key}.")

    node = bst1.tree_predecessor(bstnode_3)
    assert node.key == 2
    print(f"Tree predecessor of {bstnode_3.key} is: {node.key}.")

    # Tree deletion
    # Case 1: no children
    bst1.tree_delete(bstnode_1)
    print(f"Inorder traversal after deleting key = {bstnode_1.key}")
    inorder_tree_walk(bst1.root)

    # Case 2: one child
    bst1.tree_delete(bstnode_2)
    print(f"Inorder traversal after deleting key = {bstnode_2.key}")
    inorder_tree_walk(bst1.root)

    # Case 3: two child
    # Create a new tree because previous left/right/parent pointers are not NULL
    bst2 = BinarySearchTree()
    bstnode_4 = BinarySearchTreeNode(4)
    bstnode_5 = BinarySearchTreeNode(5)
    bstnode_6 = BinarySearchTreeNode(6)
    bst2.tree_insert(bstnode_5)
    bst2.tree_insert(bstnode_4)
    bst2.tree_insert(bstnode_6)
    inorder_tree_walk(bst2.root)
    bst2.tree_delete(bstnode_5)
    print(f"Inorder traversal after deleting key = {bstnode_5.key}")
    inorder_tree_walk(bst2.root)
    print(f"Root after deleting key = {bstnode_5.key}: {bst2.root.key}")
