"""Linked List Algorithms."""
from __future__ import absolute_import, print_function

import random
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


def insert_sorted(root: Node, value: int) -> Node:
    """Insert into linked list in sorted fashion.

    Args:
        linked_list (LinkedList): target linked list.
        node (Node): node to insert.

    Returns:
        LinkedList: target linked list.
    """
    node = Node(value)
    if not root:
        root = node

    elif root.data >= value:
        node.next = root
        root = node
    else:
        while root.next and root.next.data < value:
            root = root.next

        node.next = root.next
        root.next = node

    return root


def delete_node(root: Node, value: int) -> Node:
    """Delete Node.

    Args:
        linked_list (LinkedList): given linked list.
        value (int): value indicating the node to delete.

    Returns:
        LinkedList: result linked list.
    """
    dummy = Node(-1)
    dummy.next = root

    prev = dummy
    curr = dummy.next

    while curr and curr.data != value:
        curr = curr.next
        prev = prev.next

    if curr and curr.data == value:
        prev.next = curr.next
        curr.next = None

    return root


def compare_string(root1: Node, root2: Node) -> int:
    """Compare String.

    Args:
        s1 (Node): head of first string.
        s2 (Node): head of second string.

    Returns:
        int: 0 if same, 1 if s1 < s2, -1 if s2 < s1.
    """
    node1 = root1
    node2 = root2

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


def add_numbers(root1: Node, root2: Node) -> Node:
    """Add Numbers (Significanet Digit First).

    Args:
        root1 (Node): head of first linked list.
        root2 (Node): head of second linked list.

    Returns:
        Node: head of sum linked list.
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

    rev_l1 = reverse_list(root1)
    rev_l2 = reverse_list(root2)

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
    return sum_root


def merge_alternate(root1: Node, root2: Node) -> Union[Node, Node]:
    """Alternate Merge Linked List.

    Args:
        root1 (Node): head of first linked list.
        root2 (Node): head of second linked list.

    Returns:
        Union[Node, Node]: head of first and second linked list.
    """
    node1 = root1
    node2 = root2

    while node1 and node2:

        next1 = node1.next
        next2 = node2.next

        node1.next = node2
        node2.next = next1

        node1 = next1
        node2 = next2

        root2 = node2

    return root1, root2


def reverse_groups(root: Node, k: int) -> Node:
    """Reverse Linked List in Groups.

    Args:
        root (Node): head of linked list.
        k (int): group size

    Returns:
        Node: head of linked list.
    """

    def reverse_nodes(node, k):

        if not node:
            return None

        curr = node
        prev = None
        i = 0

        while curr and i < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        if temp:
            node.next = reverse_nodes(temp, k)

        return prev

    root = reverse_nodes(root, k)

    return root


def find_intersection_union(root1: Node, root2: Node) -> Union[set, set]:
    """Find Intersection and Union.

    Args:
        root1 (Node): head of first linked list.
        root2 (Node): head of scond linked list.

    Returns:
        Union[set, set]: intersection and union.
    """
    values = set()
    intersection = set()
    union = set()

    def helper(node, values, intersection, union):
        while node:

            if node.data in values:
                intersection.add(node.data)
            else:
                values.add(node.data)
                union.add(node.data)

            node = node.next

        return intersection, union

    helper(root1, values, intersection, union)
    helper(root2, values, intersection, union)

    return intersection, union


def detect_remove_loop(root: Node) -> Union[bool, Node]:
    """Detect and Remove Loop.

    Args:
        root (Node): head of linked list.

    Returns:
        Union[bool, Node]: loop detected, head of modified linked list.
    """
    slow, fast = root, root

    while slow and fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow.data == fast.data:

            slow = root

            while slow.next.data != fast.next.data:

                slow = slow.next
                fast = fast.next

            fast.next = None

            return True, root

    return False, root


def merge_sort(root: Node) -> Node:
    """Merge Sort.

    Args:
        root (Node): head of linked list.

    Returns:
        Node: head of sorted linked list.
    """
    if not root or not root.next:
        return root

    def get_middle(node):

        slow = node
        fast = node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = merge(a.next, b)
        else:
            result = b
            result.next = merge(a, b.next)

        return result

    mid = get_middle(root)
    mid_next = mid.next
    mid.next = None

    lt = merge_sort(root)
    rt = merge_sort(mid_next)

    sorted_list = merge(lt, rt)
    return sorted_list


def select_random(root: Node) -> Node:
    """Select Random Node.

    Args:
        root (Node): head of linked list.

    Returns:
        Node: selected node.
    """
    if not root:
        return None

    if root and not root.next:
        return root

    random.seed()
    res = root
    n = 2
    curr = root.next

    while curr:

        if random.randrange(n) == 0:
            res = curr

        curr = curr.next
        n += 1

    return res


def get_data_list(head: Node) -> List:
    """Get Data List.

    Args:
        head (Node): head of linked list.

    Returns:
        List: data list.
    """
    data = []

    while head:
        data.append(head.data)
        head = head.next

    return data


if __name__ == "__main__":

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

    list1 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(9)

    list2 = LinkedList()
    list2.insert(9)
    list2.insert(8)
    list2.insert(7)

    intersection, union = find_intersection_union(list1.head, list2.head)
    assert intersection == {9}
    assert union == {1, 2, 3, 9, 8, 7}

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

    list1 = LinkedList()
    list1.insert(50)
    list1.insert(20)
    list1.insert(15)
    list1.insert(4)
    list1.insert(10)

    head = merge_sort(list1.head)

    assert get_data_list(head) == [4, 10, 15, 20, 50]

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
