"""Run Tests."""
from __future__ import absolute_import, print_function

from array_list import ArrayList
from binary_tree import BinaryTree
from graph import Edge, Graph
from hash_table import HashTable
from heap import MinHeap
from linked_list import LinkedList
from stack_queue import Queue, Stack
from string_builder import StringBuilder
from trie import Trie


def test_graph():
    """Test Graph."""
    edges = [
        Edge(0, 1),
        Edge(0, 4),
        Edge(0, 5),
        Edge(1, 3),
        Edge(3, 2),
        Edge(3, 4),
        Edge(2, 1),
    ]
    print(edges)
    g = Graph(edges, 6)

    assert g.adj == [[1, 4, 5], [3], [1], [2, 4], [], []]


def test_min_heap():
    """Test Min Heap."""
    h = MinHeap(7)
    h.heappush(7)
    h.heappush(3)
    h.heappush(2)
    h.heappush(1)
    h.heappush(4)
    h.heappush(5)
    h.heappush(6)

    assert h.heappop() == 1
    assert h.heappop() == 2
    assert h.heappop() == 3


def test_trie():
    """Test trie."""
    t = Trie()
    t.insert("Apple")
    assert t.search("Apple")
    assert t.starts_with("App")

    t.insert("Banana")
    assert not t.search("Band")
    assert t.starts_with("Ban")


def test_binary_tree():
    """Test Binary Tree."""
    bt = BinaryTree(1)
    bt.lt = BinaryTree(2)
    bt.rt = BinaryTree(3)
    bt.lt.lt = BinaryTree(4)
    bt.lt.rt = BinaryTree(5)
    bt.rt.lt = BinaryTree(6)
    bt.rt.rt = BinaryTree(7)

    assert bt.traverse_inorder() == [4, 2, 5, 1, 6, 3, 7]
    assert bt.traverse_preorder() == [1, 2, 4, 5, 3, 6, 7]
    assert bt.traverse_postorder() == [4, 5, 2, 6, 7, 3, 1]


def test_queue():
    """Test Queue."""
    q = Queue()

    assert q.is_empty()

    q.push(1)
    assert q.arr == [1]
    assert q.peek() == 1
    assert not q.is_empty()

    q.push(1.1)
    assert q.arr == [1, 1.1]
    assert q.peek() == 1
    assert not q.is_empty()

    q.pop()
    assert q.arr == [1.1]
    assert q.peek() == 1.1
    assert not q.is_empty()

    q.pop()
    assert q.is_empty()


def test_stack():
    """Test Stack."""
    s = Stack()

    assert s.is_empty()

    s.push(1)
    assert s.arr == [1]
    assert s.top() == 1
    assert not s.is_empty()

    s.push(1.1)
    assert s.arr == [1, 1.1]
    assert s.top() == 1.1
    assert not s.is_empty()

    s.pop()
    assert s.arr == [1]
    assert s.top() == 1
    assert not s.is_empty()

    s.pop()
    assert s.is_empty()


def test_linkedlist():
    """Test LinkedList."""
    linked_list = LinkedList()

    linked_list.push(1)
    assert linked_list.head.value == 1

    linked_list.push(0)
    assert linked_list.head.value == 0

    linked_list.append(2)
    assert linked_list.head.value == 0
    assert linked_list.head.next.next.value == 2


def test_stringbuilder():
    """Test StringBuilder."""
    sb = StringBuilder()
    for _ in range(10):
        sb.append("a")

    assert str(sb) == "aaaaaaaaaa"


def test_hashtable():
    """Test HashTable."""
    ht1 = HashTable()
    ht1.add("a", "apple")
    assert ht1.get("a") == "apple"

    ht2 = HashTable()
    ht2["a"] = "apple"
    assert ht2["a"] == "apple"


def test_arraylist():
    """Test ArrayList."""
    arr = ArrayList()
    assert arr.max_size == 2
    assert arr.current_size == 0

    arr.add(1)
    arr.add(1.1)
    arr.add(-1)
    assert arr.max_size == 4
    assert arr.current_size == 3

    assert arr.get(1) == 1.1
    arr.delete(1)
    assert arr.current_size == 2
    assert arr.array == [1, -1, None, None]
