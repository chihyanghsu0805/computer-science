"""Implement LinkedList."""
# https://www.geeksforgeeks.org/linked-list-set-1-introduction/

from __future__ import absolute_import, print_function

from typing import Any


class Node:
    """Create Node Class."""

    def __init__(self, value: int = None, next: Any = None) -> None:
        """Initialize Node.

        Args:
            value (int, optional): value to store in node. Defaults to None.
            next (Any, optional): next node. Defaults to None.
        """
        self.value = value
        self.next = None


class LinkedList:
    """Create LinkedList Class."""

    def __init__(self) -> None:
        """Initialize Class."""
        self.head = None

    def print_values(self) -> None:
        """Print Values."""
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def push(self, value: int) -> None:
        """Push value to front.

        Args:
            value (int): input integer.
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value: int) -> None:
        """Append value to end.

        Args:
            value (int): input integer.
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    """
    def insert_index(self, index, value) -> None:

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            node = self.head
            for _ in range(index-1):
                if not node:
                    raise IndexError
                node = node.next

            if not node:
                self.insert_back(value)
            else:
                temp = node.next
                node.next = new_node
                new_node.next = temp
    """
