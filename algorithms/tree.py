"""Algorithms for Tree."""
from __future__ import absolute_import, print_function

from typing import List


class Node:
    """Constructor."""

    def __init__(self, value: int) -> None:
        """Initialize Class.

        Args:
            value (int): Value to store in code.
        """
        self.value = value
        self.lt = None
        self.rt = None


def find_min_depth(root: Node) -> int:
    """Find Minimum Depth.

    Args:
        root (Node): root of Tree.

    Returns:
        int: Minimum depth.
    """
    if not root:
        return 0

    queue = []
    queue.append((root, 1))

    while queue:

        node, curr_d = queue.pop(0)

        if not node.lt and not node.rt:
            return curr_d

        if node.lt:
            queue.append((node.lt, curr_d + 1))

        if node.rt:
            queue.append((node.rt, curr_d + 1))


def find_min_depth2(root: Node) -> int:
    """Find Minimum Depth.

    Args:
        root (Node): root of Tree.

    Returns:
        int: Minimum depth.
    """
    if not root:
        return 0

    if not root.lt and not root.rt:
        return 1

    if root.lt:
        lt_d = 1 + find_min_depth2(root.lt)

    if root.rt:
        rt_d = 1 + find_min_depth2(root.rt)

    return min(lt_d, rt_d)


def find_max_path_sum(root: Node) -> List:
    """Find Maximum Path Sum.

    Args:
        root (Node): Root of Tree.

    Returns:
        List: Maximum path sum, Maximum sum including root.
    """
    if not root:
        # max_so_far should not be 0 for trees with only negative values
        # max_so_far, max_end_here
        return -float("inf"), 0

    lt_so_far, lt_end_here = find_max_path_sum(root.lt)
    rt_so_far, rt_end_here = find_max_path_sum(root.rt)

    max_end_here = max(0, max(lt_end_here, rt_end_here) + root.value)
    max_so_far = max(lt_end_here + rt_end_here + root.value, lt_so_far, rt_so_far)

    return max_so_far, max_end_here


def check_array_preorder_tree(arr: List) -> bool:
    """Check Array is Preorder of Tree.

    Args:
        arr (List): Given array.

    Returns:
        bool: True if array is preorder.
    """
    stack = []
    min_value = -float("inf")

    for value in arr:

        if value < min_value:
            return False

        while len(stack) > 0 and stack[-1] < value:
            min_value = stack.pop()

        stack.append(value)

    return True


def check_full_binary_tree(root: Node) -> bool:
    """Check Full Binary Tree.

    Args:
        root (Node): root of tree.

    Returns:
        bool: tree is full.
    """
    if not root:
        return True

    if not root.lt and not root.rt:
        return True

    if root.lt and root.rt:
        return check_full_binary_tree(root.lt) and check_full_binary_tree(root.rt)

    return False


def view_bottom(root: Node) -> List:
    """View from Bottom.

    Args:
        root (Node): root of tree.

    Returns:
        List: bottom view.
    """
    if not root:
        return []

    horizontal_d = 0
    map = {}
    queue = []
    queue.append((root, horizontal_d))

    while queue:

        node, d = queue.pop(0)
        map[d] = node.value

        if node.lt:
            queue.append((node.lt, d - 1))

        if node.rt:
            queue.append((node.rt, d + 1))

    return [map[i] for i in sorted(map.keys())]


def view_top(root: Node) -> List:
    """View from Top.

    Args:
        root (Node): root of tree.

    Returns:
        List: Top view.
    """
    if not root:
        return []

    horizontal_d = 0
    map = {}
    queue = []
    queue.append((root, horizontal_d))

    while queue:

        node, d = queue.pop(0)
        if d not in map:
            map[d] = node.value

        if node.lt:
            queue.append((node.lt, d - 1))

        if node.rt:
            queue.append((node.rt, d + 1))

    return [map[i] for i in sorted(map.keys())]


if __name__ == "__main__":

    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    assert find_min_depth(root) == 2
    assert find_min_depth2(root) == 2

    root = Node(10)
    root.lt = Node(2)
    root.rt = Node(10)
    root.lt.lt = Node(20)
    root.lt.rt = Node(1)
    root.rt.rt = Node(-25)
    root.rt.rt.lt = Node(3)
    root.rt.rt.rt = Node(4)
    assert find_max_path_sum(root)[0] == 42

    arr = [40, 30, 35, 80, 100]
    assert check_array_preorder_tree(arr)
    arr = [40, 30, 35, 20, 80, 100]
    assert not check_array_preorder_tree(arr)

    root = Node(10)
    root.lt = Node(20)
    root.rt = Node(30)

    root.lt.rt = Node(40)
    root.lt.lt = Node(50)
    root.rt.lt = Node(60)
    root.rt.rt = Node(70)

    root.lt.lt.lt = Node(80)
    root.lt.lt.rt = Node(90)
    root.lt.rt.lt = Node(80)
    root.lt.rt.rt = Node(90)
    root.rt.lt.lt = Node(80)
    root.rt.lt.rt = Node(90)
    root.rt.rt.lt = Node(80)

    assert not check_full_binary_tree(root)
    root.rt.rt.rt = Node(90)
    assert check_full_binary_tree(root)

    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    root.rt.lt = Node(6)
    root.rt.rt = Node(7)
    assert view_bottom(root) == [4, 2, 6, 3, 7]
    assert view_top(root) == [4, 2, 1, 3, 7]
