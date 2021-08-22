"""Run Tests."""
from __future__ import absolute_import, print_function

from array_list import ArrayList
from hash_table import HashTable
from linked_list import LinkedList
from stack_queue import Stack
from string_builder import StringBuilder


def test_stack():
    """Test Stack."""
    s = Stack()

    assert s.is_empty

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
    assert s.is_empty


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
