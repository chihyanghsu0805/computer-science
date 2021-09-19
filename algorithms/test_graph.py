"""Test Graph Algorithms."""
from __future__ import absolute_import, print_function

from graph import (
    Edge,
    GraphList,
    GraphMatrix,
    bfs,
    dfs,
    dijkstra,
    floyd_warshall,
    union_find,
    union_find_rank,
)


def test_dfs():
    """Test DFS."""
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = GraphList(edges, 4)

    path = []

    dfs(g, 2, path)

    assert path == [2, 0, 1, 3]


def test_bfs():
    """Test BFS."""
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = GraphList(edges, 4)

    path = []

    bfs(g, 2, path)

    assert path == [2, 0, 3, 1]


def test_dijkstra():
    """Test Dijkstra."""
    g = GraphMatrix(9)
    g.adj = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]

    distance = dijkstra(g, 0)
    assert distance == [0, 4, 12, 19, 21, 11, 9, 8, 14]


def test_floyd_warshall():
    """Test Floyd Marshall."""
    g = GraphMatrix(4)
    g.adj = [
        [0, 5, float("inf"), 10],
        [float("inf"), 0, 3, float("inf")],
        [float("inf"), float("inf"), 0, 1],
        [float("inf"), float("inf"), float("inf"), 0],
    ]

    distance = floyd_warshall(g)
    assert distance == [
        [0, 5, 8, 9],
        [float("inf"), 0, 3, 4],
        [float("inf"), float("inf"), 0, 1],
        [float("inf"), float("inf"), float("inf"), 0],
    ]


def test_union_find():
    """Test Union Find."""
    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0)]
    g = GraphList(edges, 3)
    assert union_find(g)
    assert union_find_rank(g)
