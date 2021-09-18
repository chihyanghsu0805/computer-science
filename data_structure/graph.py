"""Implement Graph."""

from __future__ import absolute_import, print_function

from typing import List


class Edge:
    """Constructor."""

    def __init__(self, src: int, tar: int) -> None:
        """Initialize Class.

        Args:
            src (int): source index.
            tar (int): target index.
        """
        self.src = src
        self.tar = tar


class Graph:
    """Constructor."""

    def __init__(self, edges: List, N: int) -> None:
        """Initialize Class.

        Args:
            edge (List): List of connections [a, b] a -> b.
            N (int): number of vertices.
        """
        self.adj = [[] for _ in range(N)]

        for e in edges:
            self.adj[e.src].append(e.tar)
