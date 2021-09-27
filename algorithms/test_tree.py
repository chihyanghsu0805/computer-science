"""Test Tree Algorithms."""

from algorithms.tree import (
    Node,
    check_array_preorder_tree,
    find_max_path_sum,
    find_min_depth,
    find_min_depth2,
    view_bottom,
)


def test_find_min_depth():
    """Test Find Minimum Path."""
    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    assert find_min_depth(root) == 2
    assert find_min_depth2(root) == 2


def test_find_max_path_sum():
    """Test Find Maximum Path Sum."""
    root = Node(10)
    root.lt = Node(2)
    root.rt = Node(10)
    root.lt.lt = Node(20)
    root.lt.rt = Node(1)
    root.rt.rt = Node(-25)
    root.rt.rt.lt = Node(3)
    root.rt.rt.rt = Node(4)
    assert find_max_path_sum(root)[0] == 42


def test_check_array_preorder_tree():
    """Test Check Array Preorder Tree."""
    arr = [40, 30, 35, 80, 100]
    assert check_array_preorder_tree(arr)
    arr = [40, 30, 35, 20, 80, 100]
    assert not check_array_preorder_tree(arr)


def test_view_bottom():
    """Test View Bottom."""
    root = Node(20)
    root.lt = Node(8)
    root.rt = Node(22)
    root.lt.lt = Node(5)
    root.lt.rt = Node(3)
    root.rt.lt = Node(4)
    root.rt.rt = Node(25)
    root.lt.rt.lt = Node(10)
    root.lt.rt.rt = Node(14)
    assert view_bottom(root) == [5, 10, 4, 14, 25]
