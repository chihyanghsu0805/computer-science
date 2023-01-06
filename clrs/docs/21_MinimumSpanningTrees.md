# 21. Minimum Spinning Trees

## 21.1 Growing a minimum spanning tree

```
Generic-MST(G, w)

A = 0
while A does not from a spanning tree
    find an edge (u, v) that is safe for A
    A = A U {(u, v)}
return A
```

Loop invarant: Prior to each iteration, A is a subset of some minimum spanning tree

A cure respect  set A of edges if no edge in A crosses the cut

Light edge is an edge crossing a cut with minimum weight of any edge crossing the cut

### Exercises

21.1-1
21.1-2
21.1-3
21.1-4
21.1-5
21.1-6
21.1-7
21.1-8
21.1-9
21.1-10
21.1-11

## 21.2 The algorithms of Kruskal and Prim

Kruskal's algorithm, $O(ElogV)$
```
MST-Kruskal(G, w)
A = {}
for v in G.V
    Make-Set(v)

crate a single list of edges in G.E
sort the list of edges by weight w
for each edge (u, v)
    if Find-Set(u) != Find-Set(v)
        A = A U {(u, v)}
        Union(u, v)

return A
```

Prim's algorithm, $O(ElogV)$
```
MST-Prim(G, w, r)
for u in G.V
    u.key = INF
    u.pi = NIL

r.key = 0
Q = {}
for each u in G.V
    Insert(Q, u)

while Q
    u = Extract-Min(Q)
    for v in G.adj[u]
    if v in Q and w(u, v) < v.key
        v.pi = u
        v.key = w(u, v)
        Decrease-Key(Q, v, w(u, v))
```

Loop invariant
1.  A = {(v, v.pi): v in V - r - Q}
2.  Vertices already in MST are in V - Q
3.  for v in Q, if v.pi != NIL, then v.key < INF and v.key is the weight of a light edge (v, v.pi) connecting v to the MST

### Exercises
21.2-1
21.2-2
21.2-3
21.2-4
21.2-5
21.2-6
21.2-7
21.2-8

## Problems
21-1
21-2
21-3
21-4
