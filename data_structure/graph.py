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


def dfs(g: Graph, root: int, path: List) -> List:
    """Depth First Search.

    Args:
        g (Graph): Graph to search in.
        src (int): source node.
        path (List): search path.

    Returns:
        List: sequence of search.
    """
    path.append(root)

    for tar in g.adj[root]:
        if tar not in path:
            dfs(g, tar, path)


def bfs(g: Graph, root: int, path: List) -> List:
    """Bredth First Search.

    Args:
        g (Graph): Graph to search in.
        src (int): source node.
        path (List): search path.

    Returns:
        List: sequence of search.
    """
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        path.append(node)
        for nbor in g.adj[node]:
            if nbor not in path:
                queue.append(nbor)


if __name__ == "__main__":
    edges = [
        Edge(0, 1),
        Edge(0, 4),
        Edge(0, 5),
        Edge(1, 3),
        Edge(3, 2),
        Edge(3, 4),
        Edge(2, 1),
    ]
    g = Graph(edges, 6)
    path = []
    dfs(g, 0, path)
    print(path)

    path = []
    bfs(g, 0, path)
    print(path)
