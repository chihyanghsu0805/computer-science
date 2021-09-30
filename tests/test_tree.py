"""Test Tree Algorithms."""

from algorithms.tree import (
    Node,
    check_array_preorder_tree,
    check_subtree,
    find_lowest_common_ancestor,
    find_max_path_sum,
    find_min_depth,
    find_min_depth2,
    inorder,
    remove_node_on_path,
    reverse_alternate_level,
    view_bottom,
    view_top,
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


def test_view_top():
    """Test View Top."""
    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    root.rt.lt = Node(6)
    root.rt.rt = Node(7)
    assert view_top(root) == [4, 2, 1, 3, 7]


def test_remove_node_on_path():
    """Test Remove Node on Path."""
    k = 4
    root = Node(1)
    root.lt = Node(2)
    root.rt = Node(3)
    root.lt.lt = Node(4)
    root.lt.rt = Node(5)
    root.lt.lt.lt = Node(7)
    root.rt.rt = Node(6)
    root.rt.rt.lt = Node(8)

    assert inorder(remove_node_on_path(root, k)) == [7, 4, 2, 1, 3, 8, 6]


def test_find_lowest_common_ancestor():
    """Test Find Lowest Common Ancestor."""
    root = Node(20)
    root.lt = Node(8)
    root.rt = Node(22)
    root.lt.lt = Node(4)
    root.lt.rt = Node(12)
    root.lt.rt.lt = Node(10)
    root.lt.rt.rt = Node(14)
    v1, v2 = 10, 14
    assert find_lowest_common_ancestor(root, v1, v2).value == 12
    v1, v2 = 8, 14
    assert find_lowest_common_ancestor(root, v1, v2).value == 8
    v1, v2 = 10, 22
    assert find_lowest_common_ancestor(root, v1, v2).value == 20


def test_check_subtree():
    """Test Check Subtree."""
    root1 = Node("A")
    root1.lt = Node("B")
    root1.rt = Node("D")
    root1.lt.lt = Node("C")
    root1.rt.rt = Node("E")

    root2 = Node("A")
    root2.lt = Node("B")
    root2.rt = Node("D")
    root2.lt.lt = Node("C")

    assert not check_subtree(root2, root1)


def test_reverse_alternate_level():
    """Test Reverse Alternate Level."""
    root = Node("a")
    root.lt = Node("b")
    root.rt = Node("c")
    root.lt.lt = Node("d")
    root.lt.rt = Node("e")
    root.rt.lt = Node("f")
    root.rt.rt = Node("g")
    root.lt.lt.lt = Node("h")
    root.lt.lt.rt = Node("i")
    root.lt.rt.lt = Node("j")
    root.lt.rt.rt = Node("k")
    root.rt.lt.lt = Node("l")
    root.rt.lt.rt = Node("m")
    root.rt.rt.lt = Node("n")
    root.rt.rt.rt = Node("o")

    reverse_alternate_level(root)
    assert inorder(root) == [
        "o",
        "d",
        "n",
        "c",
        "m",
        "e",
        "l",
        "a",
        "k",
        "f",
        "j",
        "b",
        "i",
        "g",
        "h",
    ]
