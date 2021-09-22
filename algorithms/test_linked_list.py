"""Test Linked List Algorithms."""
from __future__ import absolute_import, print_function

from algorithms.linked_list import (
    LinkedList,
    Node,
    add_numbers,
    compare_string,
    delete_node,
    insert_sorted,
)


def test_insert_sorted():
    """Test sorted insert."""
    linked_list = LinkedList()
    assert linked_list.store_data_list() == []

    node = Node(5)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [5]

    node = Node(10)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [5, 10]

    node = Node(3)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [3, 5, 10]


def test_delete_node():
    """Test Delete Node."""
    linked_list = LinkedList()
    assert linked_list.store_data_list() == []

    node = Node(5)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [5]

    node = Node(10)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [5, 10]

    node = Node(3)
    linked_list = insert_sorted(linked_list, node)
    assert linked_list.store_data_list() == [3, 5, 10]

    linked_list = delete_node(linked_list, 5)
    assert linked_list.store_data_list() == [3, 10]


def test_compare_string():
    """Test Compare String."""
    list1 = LinkedList()
    list1.insert("g")
    list1.insert("e")
    list1.insert("e")
    list1.insert("k")
    list1.insert("s")
    list1.insert("b")

    list2 = LinkedList()
    list2.insert("g")
    list2.insert("e")
    list2.insert("e")
    list2.insert("k")
    list2.insert("s")
    list2.insert("a")

    assert compare_string(list1, list2) == -1


def test_add_numbers():
    """Test Add Numbers."""
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)

    list2 = LinkedList()
    list2.insert(9)
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)

    _sum = add_numbers(list1, list2)
    assert _sum.store_data_list() == [1, 0, 1, 1, 0]
