"""Contain tree algorithms."""
import copy

from clrs.data_structures.binary_tree import BinaryTreeNode
from clrs.data_structures.red_black_tree import RedBlackTreeNode

__all__ = [
    "inorder_tree_walk",
    "validate_binary_search_tree",
    "validate_red_black_tree",
]


def validate_red_black_tree(x: RedBlackTreeNode) -> bool:
    """Validate red black tree properties.

    Args:
        x (RedBlackTreeNode): root of red black tree.

    Returns:
        bool: True if properties maintained.
    """
    bool_rb = True

    # Property 0: Red black tree must be binary search tree
    bst_x = copy.deepcopy(x)
    bst_x = remove_nil(bst_x)
    p0 = validate_binary_search_tree(bst_x, float("inf"), -float("inf"))
    bool_rb &= p0

    # Property 2: Root is BLACK
    p2 = x.color == "B"
    bool_rb &= p2

    bool_rb &= validate_red_black_path(x)
    return bool_rb


def remove_nil(x: RedBlackTreeNode) -> RedBlackTreeNode:
    """Remove NIL from Red Black tree for validation.

    Args:
        x (RedBlackTreeNode): a red black tree node.

    Returns:
        RedBlackTreeNode: a red black tree node.
    """
    if x.key == -1:
        return None

    x.left = remove_nil(x.left)
    x.right = remove_nil(x.right)

    return x


def validate_red_black_path(x: RedBlackTreeNode) -> bool:
    """Validate red black properties in path.

    Args:
        x (RedBlackTreeNode): a red black tree node.

    Returns:
        bool: True if properties maintained.
    """
    # Property 1: Every node is either RED or BLACK
    if x.color != "R" and x.color != "B":
        return False

    # Property 3: Leaf is BLACK
    if x.key == -1:
        return x.color == "B"

    # Property 4: If node is red, both children are BLACK
    if x.color == "R" and (x.left.color != "B" or x.right.color != "B"):
        return False

    left_bh = count_black_height(x.left)
    right_bh = count_black_height(x.right)
    return left_bh == right_bh


def count_black_height(x: RedBlackTreeNode) -> int:
    """Count black height, number of black nodes in path exclude self.

    Args:
        x (RedBlackTreeNode): a red black tree node.

    Returns:
        int: black height.
    """
    if x.key == -1:
        return 0

    if x.color == "B":
        return 1

    left_bh = count_black_height(x.left)
    if x.left.color == "B":
        left_bh += 1
    right_bh = count_black_height(x.right)
    if x.right.color == "B":
        right_bh += 1

    return left_bh if left_bh == right_bh else -1


def inorder_tree_walk(x: BinaryTreeNode) -> None:
    """Traverse tree inorder.

    Args:
        x (BinaryTreeNode): node.
    """
    if not x:
        return

    inorder_tree_walk(x.left)
    print(x.key)
    inorder_tree_walk(x.right)

    return


def validate_binary_search_tree(x: BinaryTreeNode, _max: float, _min: float) -> bool:
    """Validate binary search tree propery of x.left.ley < x.key < x.right.key.

    Args:
        x (BinaryTreeNode): binary search tree node.
        _max (float): maximum value.
        _min (float): minimum value.

    Returns:
        bool: True if property maintained.
    """
    # https://leetcode.com/problems/validate-binary-search-tree/
    if not x:
        return True

    if x.key >= _max:
        return False

    if x.key <= _min:
        return False

    bool_left = validate_binary_search_tree(x.left, x.key, _min)
    bool_right = validate_binary_search_tree(x.right, _max, x.key)

    return bool_left and bool_right
