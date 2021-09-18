"""Test Graph Algorithms."""
from __future__ import absolute_import, print_function

from graph import Edge, Graph, bfs, dfs


def test_dfs():
    """Test DFS."""
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = Graph(edges, 4)

    path = []

    dfs(g, 2, path)

    assert path == [2, 0, 1, 3]


def test_bfs():
    """Test BFS."""
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = Graph(edges, 4)

    path = []

    bfs(g, 2, path)

    assert path == [2, 0, 3, 1]
