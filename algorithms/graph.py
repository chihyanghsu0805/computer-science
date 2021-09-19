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


class GraphMatrix:
    """Constructor."""

    def __init__(self, vertices: int) -> None:
        """Initialize Class.

        Args:
            vertices (int): number of vertices.
        """
        self.V = vertices
        self.adj = [[0 for _ in range(vertices)] for _ in range(vertices)]


class GraphList:
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


def dfs(graph: GraphList, node: int, path: List):
    """Depth First Search.

    Args:
        graph (GraphList): graph with adjacency list.
        node (int): root node.
        path (List): path with visted nodes.
    """
    if node in path:
        return

    path.append(node)

    for nbor in graph.adj[node]:
        dfs(graph, nbor, path)


def bfs(graph: GraphList, root: int, path: List):
    """Breadth First Search.

    Args:
        graph (GraphList): graph with adjacency list.
        root (int): root node.
        path (List): path with visited nodes.
    """
    queue = []
    queue.append(root)

    while queue:

        node = queue.pop(0)

        if node in path:
            continue
        else:
            path.append(node)

            for nbor in graph.adj[node]:
                queue.append(nbor)


def dijkstra(graph: GraphMatrix, source: int) -> List:
    """Dijkstra.

    Args:
        graph (GraphMatrix): Graph with adjacency matrix.
        source (int): source vertex.

    Returns:
        List: distance array.
    """
    distance = [float("inf")] * graph.V
    distance[source] = 0
    visited = [False] * graph.V

    def min_distance(distance, visited):
        minimum = float("inf")
        for u in range(graph.V):
            if distance[u] < minimum and not visited[u]:
                minimum = distance[u]
                min_index = u

        return min_index

    for _ in range(graph.V):

        priority_node = min_distance(distance, visited)
        visited[priority_node] = True

        for next_node in range(graph.V):

            if (
                graph.adj[priority_node][next_node] > 0
                and not visited[next_node]
                and distance[next_node]
                > distance[priority_node] + graph.adj[priority_node][next_node]
            ):
                distance[next_node] = (
                    distance[priority_node] + graph.adj[priority_node][next_node]
                )

    return distance


def floyd_warshall(graph: GraphMatrix) -> List:
    """Floyd Warshall.

    Args:
        graph (GraphMatrix): graph with adjacency matrix.

    Returns:
        List: distance array.
    """
    distance = []

    for r in range(len(graph.adj)):
        distance.append(graph.adj[r])

    for k in range(graph.V):
        for i in range(graph.V):
            for j in range(graph.V):

                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 0), Edge(2, 3), Edge(3, 3)]
    g = GraphList(edges, 4)

    path = []
    dfs(g, 2, path)
    assert path == [2, 0, 1, 3]

    path = []
    bfs(g, 2, path)
    assert path == [2, 0, 3, 1]

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
