"""Test Linked List Algorithms."""
from __future__ import absolute_import, print_function

from algorithms.linked_list import (
    LinkedList,
    add_numbers,
    compare_string,
    delete_node,
    detect_remove_loop,
    find_intersection_union,
    get_data_list,
    insert_sorted,
    merge_alternate,
    merge_sort,
    reverse_groups,
    select_random,
)


def test_insert_sorted():
    """Test sorted insert."""
    list1 = LinkedList()
    assert get_data_list(list1.head) == []

    list1.head = insert_sorted(list1.head, 5)
    assert get_data_list(list1.head) == [5]

    list1.head = insert_sorted(list1.head, 10)
    assert get_data_list(list1.head) == [5, 10]

    list1.head = insert_sorted(list1.head, 3)
    assert get_data_list(list1.head) == [3, 5, 10]


def test_delete_node():
    """Test Delete Node."""
    list1 = LinkedList()
    assert get_data_list(list1.head) == []

    list1.head = insert_sorted(list1.head, 5)
    assert get_data_list(list1.head) == [5]

    list1.head = insert_sorted(list1.head, 10)
    assert get_data_list(list1.head) == [5, 10]

    list1.head = insert_sorted(list1.head, 3)
    assert get_data_list(list1.head) == [3, 5, 10]

    list1.head = delete_node(list1.head, 5)
    assert get_data_list(list1.head) == [3, 10]


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

    assert compare_string(list1.head, list2.head) == -1


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

    _sum = add_numbers(list1.head, list2.head)
    assert get_data_list(_sum) == [1, 0, 1, 1, 0]


def test_merge_alternate():
    """Test Merge Alternate."""
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)

    list2 = LinkedList()
    list2.insert(9)
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)

    merged_l1, merged_l2 = merge_alternate(list1.head, list2.head)
    assert get_data_list(merged_l1) == [1, 9, 2, 9, 3, 8]
    assert get_data_list(merged_l2) == [7]


def test_reverse_groups():
    """Test Reverse Groups."""
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(9)
    list1.insert(9)
    list1.insert(8)
    list1.insert(7)

    reversed = reverse_groups(list1.head, 3)
    assert get_data_list(reversed) == [3, 2, 1, 8, 9, 9, 7]


def test_find_intersection_union():
    """Test Find Intersection and Union."""
    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(9)

    list2 = LinkedList()
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)

    intersection, union = find_intersection_union(list1, list2)
    assert intersection.store_data_list() == [9]
    assert union.store_data_list() == [1, 2, 3, 9, 8, 7]


def test_detect_remove_loop():
    """Test Detect and Remove Loop."""
    list1 = LinkedList()
    list1.insert(50)
    list1.insert(20)
    list1.insert(15)
    list1.insert(4)
    list1.insert(10)

    bool1, head1 = detect_remove_loop(list1.head)

    assert not bool1
    assert get_data_list(head1) == [50, 20, 15, 4, 10]

    list1.head.next.next.next.next.next = list1.head.next.next
    bool2, head2 = detect_remove_loop(list1.head)

    assert bool2
    assert get_data_list(head2) == [50, 20, 15, 4, 10]


def test_merge_sort():
    """Test Merge Sort."""
    list1 = LinkedList()
    list1.insert(50)
    list1.insert(20)
    list1.insert(15)
    list1.insert(4)
    list1.insert(10)

    head = merge_sort(list1.head)

    assert get_data_list(head) == [4, 10, 15, 20, 50]


def test_select_random():
    """Test Select Random."""
    list1 = LinkedList()
    list1.insert(5)
    list1.insert(20)
    list1.insert(4)
    list1.insert(3)
    list1.insert(30)

    res_freq = {}

    for _ in range(10000):
        val = select_random(list1.head).data
        res_freq[val] = res_freq.get(val, 0) + 1

    res_prob = [x / 10000 for x in res_freq.values()]
    assert all([x < 0.25 for x in res_prob])
    assert all([x > 0.15 for x in res_prob])
