# 22. Single Source Shortest Paths

-   Single-destination shortest-paths problem
-   Single-pair shortest-paths problem
-   All-pair shortest-paths problem
-   Negative weights are okay, not negative weight cycles nor positive weight cycles
-   Relaxation v.d upper bound on the weight of a shortest path from source s to v, shortest path estimate

```
Relax(u, v, w)
if v.d > u.d + w(u, v)
    v.d = u.d + w(u, v)
    v.pi = u
```
-   Triangle inequality
-   Upper-bound property
-   No-path property
-   Convergence property
-   Path-relaxation property
-   Predecessor-subgraph property

## 22.1 The Bellman-Ford algorithm

Single source shortest paths problem

$O(V^2 + VE)$

```
Bellman-Ford(G, w, s)
Initialize-Single-Source(G, s)
for i = 1 to |G.V| - 1
    for each edge (u, v) in G.E
        RElax(u, v, w)

for (u, v) in G.E
    if v.d > u.d + w(u, v)
        return False

return True
```

### Exercises
22.1-1
22.1-2
22.1-3
22.1-4
22.1-5
22.1-6
22.1-7

## 22.2 Single-source shortest paths in directed acyclic graphs

$\Theta(V + E)$

```
DAG-Shortest-Paths(G, w, s)
topologically sort the vertices of G
Initialize-Single-Source(G, s)
for u in G.V in toplogically sorted order
    for v in G.adj[u]
        Relax(u, v, w)
```

Program Evaluation and Review Technique (PERT)

Critical path is a longest path through the dag, and can be found by
-   negating the edge weights and running DAG-Shortest-Paths
-   running DAG-Shortest-Paths but replace INF with -INF in Initialize-Songle-Source and > by < in Relax

### Exercises
22.2-1
22.2-2
22.2-3
22.2-4

## 22.3 Dijkstra's algorithm

```
Dijkstra(G, w, s)
Initializa-Single-Source(G, s)
S = {}
Q = {}

for u in G.V
    Insert(Q, u)

while Q is not empty
    u = Extract-Min(Q)
    S = S U {u}
    for v in G.adj[u]
        Relax(u, v, w)
        if v.d decreased by Relax
            Decreas-Key(Q, v, v.d)
```

### Exercises
22.3-1
22.3-2
22.3-3
22.3-4
22.3-5
22.3-6
22.3-7
22.3-8
22.3-9
22.3-10
22.3-11
22.3-12

## 22.4 Difference constraints and shortest paths

Linear programming

Constraint graph

### Exercises
22.4-1
22.4-2
22.4-3
22.4-4
22.4-5
22.4-6
22.4-7
22.4-8
22.4-9
22.4-10
22.4-11
22.4-12

## 22.5 Proofs of shortest-paths properties

### Exercises
22.5-1
22.5-2
22.5-3
22.5-4
22.5-5
22.5-6
22.5-7
22.5-8

## Problems
22-1
22-2
22-3
22-4
22-5
22-6
