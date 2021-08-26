"""Implement Min Heap."""
# https://www.askpython.com/python/examples/min-heap

from __future__ import absolute_import, print_function

import sys
from numbers import Number


class MinHeap:
    """Constructor."""

    def __init__(self, max_size: int) -> None:
        """Initialize Class.

        Args:
            max_size (int): maximum heap size.
        """
        self.max_size = max_size
        self.current_size = 0
        self.heap = [0] * (self.max_size + 1)
        self.heap[0] = sys.maxsize * -1
        self.root = 1

    def min_heapify(self, i: int):
        """Heapify Min Heap.

        Args:
            i (int): index.
        """
        if not (i >= (self.current_size // 2) and i <= self.current_size):
            if self.heap[i] > self.heap[2 * i] or self.heap[i] > self.heap[(2 * i) + 1]:
                if self.heap[2 * i] < self.heap[(2 * i) + 1]:
                    self.swapnodes(i, 2 * i)
                    self.min_heapify(2 * i)
                else:
                    self.swapnodes(i, (2 * i) + 1)
                    self.min_heapify((2 * i) + 1)

    def heappush(self, element: Number) -> None:
        """Push element to heap.

        Args:
            element (Number): Element to be pushed.
        """
        if self.current_size > self.max_size:
            return

        self.current_size += 1
        self.heap[self.current_size] = element
        current = self.current_size

        while self.heap[current] < self.heap[current // 2]:
            self.swapnodes(current, current // 2)
            current = current // 2

    def swapnodes(self, node1: int, node2: int) -> None:
        """Swap nodes.

        Args:
            node1 (int): first node.
            node2 (int): second node.
        """
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    def heappop(self) -> Number:
        """Pop top of heap.

        Returns:
            Number: value from top of heap.
        """
        last = self.heap[self.root]
        self.heap[self.root] = self.heap[self.current_size]
        self.current_size -= 1
        self.min_heapify(self.root)
        return last
