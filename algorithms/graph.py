"""Graph Algorithms."""
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


def dfs(graph: Graph, node: int, path: List):
    """Depth First Search.

    Args:
        graph (Graph): graph with adjacency list.
        node (int): root node.
        path (List): path with visted nodes.
    """
    if node in path:
        return

    path.append(node)

    for nbor in graph.adj[node]:
        dfs(graph, nbor, path)


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = Graph(edges, 4)

    path = []

    dfs(g, 2, path)

    assert path == [2, 0, 1, 3]
