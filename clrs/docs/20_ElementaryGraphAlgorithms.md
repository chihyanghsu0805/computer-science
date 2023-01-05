# 20. Elementary Graph Problems

## 20.1 Representation of graphs

-   Adjacency list: sparse, $\Theta_S(V + E)$, $\Theta_T(V + E)$ for finding each edge
-   Adjacency graph: dense, $\Theta_S(V x V)$, $\Theta_T(V + V)$ for finding each edge

### Exercises

20.1-1
20.1-2
20.1-3
20.1-4
20.1-5
20.1-6
20.1-7
20.1-8

## 20.2 Breadth first search

Shortest paths

### Exercises

20.2-1
20.2-2
20.2-3
20.2-4
20.2-5
20.2-6
20.2-7
20.2-8

## 20.3 Depth first search

u.d discovery time < u.f finish time

Parenthsis structure

Parenthsis theorem, one of the following three condition holds
-   intervals [u.d, u.f] and [v.d, v.f] are entirely disjoint, and neither u nor v is a descendant of the other in the depth first forest
-   the interval [u.d, u.f] is contained entirely within the interval [v.d, v.f], and u is a descendant of v in a depth first tree
-   the interval [v.d, v.f] is contained entirely within the interval [u.d, u.f], and v is a descendant of u in a depth first tree

Classification of edges
-   Tree edges: (u, v) is a tree edge if v is first discovered by exploring edge (u, v)
-   Back edges: (u, v) connects u back to an ancestor v, also self loops
-   Forward edges: (u, v) is a nontree edge connecting to a proper descendant
-   Cross edges: all other edges, connecting different trees, or same tree with one vertex not an ancestor of the other

### Exercises

20.3-1
20.3-2
20.3-3
20.3-4
20.3-5
20.3-6
20.3-7
20.3-8
20.3-9
20.3-10
20.3-11
20.3-12
20.3-13

## 20.4 Topological sort

Acyclic DAG with vertices appear in reverse order of their finishing time, $\Theta(V + E)$

### Exercises

20.4-1
20.4-2
20.4-3
20.4-4
20.4-5

## 20.5 Strongly connected components

call DFS($G$) to compute finish times u.f

create $G^T$

call DFS($G^T$) in order of decreasing u.f

vertices of each tree os a separate strongly connected component

### Exercises

20.5-1
20.5-2
20.5-3
20.5-4
20.5-5
20.5-6
20.5-7
20.5-8

## Problems

20-1
20-2
20-3
20-4
20-5
