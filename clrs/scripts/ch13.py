"""Contain implementation for chapter 13."""

import sys

sys.path.append("../../")

from clrs.algorithms.trees import inorder_tree_walk, validate_red_black_tree
from clrs.data_structures.red_black_tree import RedBlackTree, RedBlackTreeNode

if __name__ == "__main__":

    rbnode_1 = RedBlackTreeNode(1)
    rbnode_2 = RedBlackTreeNode(2)
    rbnode_3 = RedBlackTreeNode(3)

    # Tree insertion
    rbt = RedBlackTree()
    rbt.tree_insert(rbnode_1)
    rbt.tree_insert(rbnode_2)
    rbt.tree_insert(rbnode_3)

    # Validate red black tree property
    bool_rbt_property = validate_red_black_tree(rbt.root)
    print(f"Tree obeys Red Black Tree property: {bool_rbt_property}")

    # Inorder
    print("Inorder traversal of Red Black Tree gives sorted keys:")
    inorder_tree_walk(rbt.root)
