"""Graph Algorithms."""
from __future__ import absolute_import, print_function

from typing import List


class Edge:
    """Constructor."""

    def __init__(self, source: int, target: int) -> None:
        """Initialize Class.

        Args:
            source (int): source vertex.
            target (int): target vertex.
        """
        self.source = source
        self.target = target


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
        self.V = N
        self.adj = [[] for _ in range(N)]

        for e in edges:
            self.adj[e.source].append(e.target)


class GraphListWeight:
    """Constructor."""

    def __init__(self, vertices: int) -> None:
        """Initialize Class.

        Args:
            vertices (int): number of vertices.
        """
        self.V = vertices
        self.adj = []

    def add_edge(self, u: int, v: int, w: float) -> None:
        """Add Edge.

        Args:
            u (int): source vertex index.
            v (int): target vertex index.
            w (float): edge weight.
        """
        self.adj.append([u, v, w])


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


def union_find(graph: GraphList) -> bool:
    """Union Find.

    Args:
        graph (GraphList): graph with adjacency list.

    Returns:
        bool: whether graph contains cycle.
    """
    parent = [-1] * graph.V

    def find_parent(parent, i):
        if parent[i] == -1:
            return i

        return find_parent(parent, parent[i])

    def union(parent, x, y):
        parent[x] = y

    for i, vertices in enumerate(graph.adj):
        for j in vertices:
            x = find_parent(parent, i)
            y = find_parent(parent, j)

            if x == y:
                return True

            union(parent, x, y)
    return False


def union_find_rank(graph: GraphList) -> bool:
    """Union Find with Rank and Path Compression.

    Args:
        graph (GraphList): graph with adjacency list.

    Returns:
        bool: whether graph contains cycle.
    """
    parent = []
    for u in range(graph.V):
        parent.append([u, 0])  # list[parent, rank]

    def find_parent(parent, i):
        if parent[i][0] != i:
            parent[i][0] = find_parent(parent, parent[i][0])
        return parent[i][0]

    def union(parent, x, y):

        if parent[x][1] > parent[y][1]:
            parent[y][0] = x
        elif parent[x][1] < parent[y][1]:
            parent[x][0] = y
        else:
            parent[y][0] = x
            parent[x][1] += 1

    for i, vertices in enumerate(graph.adj):
        x = find_parent(parent, i)

        for j in vertices:
            y = find_parent(parent, j)

            if x == y:
                return True

            union(parent, x, y)
    return False


def prim(graph: GraphMatrix) -> List:
    """Prim.

    Args:
        graph (GraphMatrix): Graph with adjacency matrix.

    Returns:
        List: list describing [parent, node, weight].
    """
    min_span_tree = [False for _ in range(graph.V)]
    parent = [None] * graph.V
    parent[0] = -1

    key = [float("inf") for _ in range(graph.V)]
    key[0] = 0

    def find_priority_vertex(min_span_tree, key):
        min_k = float("inf")
        min_idx = -1
        for idx, k in enumerate(key):
            if not min_span_tree[idx] and k < min_k:
                min_idx = idx
                min_k = k

        return min_idx

    for u in range(graph.V):

        vertex = find_priority_vertex(min_span_tree, key)
        min_span_tree[vertex] = True

        for v in range(graph.V):

            if (
                graph.adj[u][v] > 0
                and not min_span_tree[v]
                and graph.adj[u][v] < key[v]
            ):
                key[v] = graph.adj[u][v]
                parent[v] = u

    res = []
    for i in range(graph.V):
        res.append([parent[i], i, key[i]])

    return res


def kruskal(graph: GraphListWeight) -> List:
    """Kruskal.

    Args:
        graph (GraphListWeight): Graph with weighted adjacency list.

    Returns:
        List: list describing [parent, vertex, weight]
    """
    i, e = 0, 0
    parent, rank, res = [], [], []
    graph.adj = sorted(graph.adj, key=lambda x: x[2])

    def find_parent(parent, u):
        if parent[u] != u:
            parent[u] = find_parent(parent, parent[u])
        return parent[u]

    def union(parent, rank, x, y):
        x_root = find_parent(parent, x)
        y_root = find_parent(parent, y)

        if rank[x_root] > rank[y_root]:
            parent[y] = x
        elif rank[x_root] < rank[y_root]:
            parent[x] = y
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    for vertex in range(graph.V):
        parent.append(vertex)
        rank.append(0)

    while e < graph.V - 1:
        u, v, w = graph.adj[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            e += 1
            res.append([u, v, w])
            union(parent, rank, x, y)

    return res


def topological_sort(graph: GraphList) -> List:
    """Topological Sort.

    Args:
        graph (GraphList): Graph with adjacency list.

    Returns:
        List: topological sort of graph.
    """
    visited = [False] * graph.V
    stack = []

    def topological_sort_helper(i, visited, sort):
        visited[i] = True
        for j in graph.adj[i]:
            if not visited[j]:
                topological_sort_helper(j, visited, stack)
        stack.append(i)

    for i in range(graph.V):
        if not visited[i]:
            topological_sort_helper(i, visited, stack)

    return stack[::-1]


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

    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0)]
    g = GraphList(edges, 3)
    assert union_find(g)
    assert union_find_rank(g)

    g = GraphMatrix(5)
    g.adj = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    assert prim(g) == [[-1, 0, 0], [0, 1, 2], [1, 2, 3], [0, 3, 6], [1, 4, 5]]

    g = GraphListWeight(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    assert kruskal(g) == [[2, 3, 4], [0, 3, 5], [0, 1, 10]]

    edges = [Edge(5, 2), Edge(5, 0), Edge(4, 0), Edge(4, 1), Edge(2, 3), Edge(3, 1)]
    g = GraphList(edges, 6)
    assert topological_sort(g) == [5, 4, 2, 3, 1, 0]
