"""Linked List Algorithms."""
from __future__ import absolute_import, print_function

from typing import List, Union


class Node:
    """Constructor."""

    def __init__(self, data: any) -> None:
        """Initialize Class.

        Args:
            data (any): data to store in node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Constructor."""

    def __init__(self) -> None:
        """Initialize Class."""
        self.head = None

    def insert(self, value: any) -> None:
        """Insert.

        Args:
            value (any): value to be inserted.
        """
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            root = self.head
            while root.next:
                root = root.next
            root.next = node

    def store_data_list(self) -> List:
        """Store data in a list.

        Returns:
            List: data list.
        """
        data = []
        root = self.head

        while root:
            data.append(root.data)
            root = root.next

        return data


def insert_sorted(linked_list: LinkedList, node: Node) -> LinkedList:
    """Insert into linked list in sorted fashion.

    Args:
        linked_list (LinkedList): target linked list.
        node (Node): node to insert.

    Returns:
        LinkedList: target linked list.
    """
    if not linked_list.head:
        linked_list.head = node

    elif linked_list.head.data >= node.data:
        node.next = linked_list.head
        linked_list.head = node
    else:
        root = linked_list.head
        while root.next and root.next.data < node.data:
            root = root.next

        node.next = root.next
        root.next = node

    return linked_list


def delete_node(linked_list: LinkedList, value: int) -> LinkedList:
    """Delete Node.

    Args:
        linked_list (LinkedList): given linked list.
        value (int): value indicating the node to delete.

    Returns:
        LinkedList: result linked list.
    """
    dummy = Node(-1)
    dummy.next = linked_list.head

    prev = dummy
    curr = dummy.next

    while curr and curr.data != value:
        curr = curr.next
        prev = prev.next

    if curr and curr.data == value:
        prev.next = curr.next
        curr.next = None

    return linked_list


def compare_string(s1: LinkedList, s2: LinkedList) -> int:
    """Compare String.

    Args:
        s1 (LinkedList): first string.
        s2 (LinkedList): second string.

    Returns:
        int: 0 if same, 1 if s1 < s2, -1 if s2 < s1.
    """
    node1 = s1.head
    node2 = s2.head

    while node1 and node2 and node1.data == node2.data:
        node1 = node1.next
        node2 = node2.next

    if not node1 and not node2:
        return 0

    if not node1:
        return 1

    if not node2:
        return -1

    if node1.data < node2.data:
        return 1

    if node1.data == node2.data:
        return 0

    if node1.data > node2.data:
        return -1


def add_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """Add Numbers.

    Args:
        l1 (LinkedList): first linked list.
        l2 (LinkedList): second linked list.

    Returns:
        LinkedList: linked list storing sum.
    """

    def reverse_list(root):

        node = root
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev

    rev_l1 = reverse_list(l1.head)
    rev_l2 = reverse_list(l2.head)

    def compute_sum(l1, l2):

        dummy = Node(0)
        node = dummy

        n1 = l1
        n2 = l2
        carry = 0

        while n1 or n2 or carry:
            v1 = n1.data if n1 else 0
            v2 = n2.data if n2 else 0
            _sum = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            node.next = Node(_sum)
            node = node.next
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

        return dummy.next

    _sum = compute_sum(rev_l1, rev_l2)
    sum_root = reverse_list(_sum)
    node = sum_root
    sum_list = LinkedList()
    while node:
        sum_list.insert(node.data)
        node = node.next
    return sum_list


def merge_alternate(l1: LinkedList, l2: LinkedList) -> Union[LinkedList, LinkedList]:
    """Merge Alternate.

    Args:
        l1 (LinkedList): first linked list.
        l2 (LinkedList): second linked list.

    Returns:
        Union[LinkedList, LinkedList]: merged first and second linked list.
    """
    node1 = l1.head
    node2 = l2.head

    while node1 and node2:

        next1 = node1.next
        next2 = node2.next

        node1.next = node2
        node2.next = next1

        node1 = next1
        node2 = next2

        l2.head = node2

    return l1, l2


if __name__ == "__main__":

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

    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)

    list2 = LinkedList()
    list2.insert(9)
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)

    merged_l1, merged_l2 = merge_alternate(list1, list2)
    assert merged_l1.store_data_list() == [1, 9, 2, 9, 3, 8]
    assert merged_l2.store_data_list() == [7]
