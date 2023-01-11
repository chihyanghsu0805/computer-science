# 23. All-Pairs Shortest Paths

## 23.1 Shortest paths and matrix multiplication

```
Extend-Shortest-Paths(L<sup>(r-1)</sup>, W, L<sup>r</sup>, n)
for i = 1 to n
    for j = 1 to n
        for k = 1 to n
            l_(ij)^r = min{l_(ij)^r, l_(ik)^(r-1) + w_kj}
```

```
Slow-APSP(W, L^(0), n)
L = L^0
M = NxN
for r = 1 to n - 1
    M = INF
    Extend-Shortest-Paths(L, W, M, n)
    L = M

return L
```

```
Faster-ASAP(W, n)
L = W
M = NxN
r = 1
while r < n - 1
    M = INF
    Extend-Shortest-Paths(L, L, M, n)
    r = 2 * r
    L = M

return L
```

### Exercises
23.1-1
23.1-2
23.1-3
23.1-4
23.1-5
23.1-6
23.1-7
23.1-8
23.1-9
23.1-10

## 23.2 The Floyd-Warshall algorithm

```
Floyd-Warshall(W, n)
D^0 = W
for k = 1 to n
    D^k = NxN
    for i = 1 to n
        for j = 1 to n
            d_(ij)^k = min{d_(ij)^(k-1), d_(ik)^(k-1) + d_(kj)^(k-1)}

return D^n
```

Transistive closure of a directed graph
Whether there is a path from i to j in G

```
Transistive-Closure(G, n)
T^0 = NxN
for i = 1 to n
    for j = 1 to n
        if i == j or (i, j) in G.E
            t_(ij)^0 = 1
        else
            t_(ij)^0 = 0

for k = 1 to n
    T^k = NxN
    for i = 1 to n
        for j = 1 to n
            t_(ij)^k  = t_(ij)^(k-1) UNION (t_(ik)^(k-1) INTERSECT t_(kj)^(k-1))

return T(n)
```

### Exercises
23.2-1
23.2-2
23.2-3
23.2-4
23.2-5
23.2-6
23.2-7
23.2-8
23.2-9
