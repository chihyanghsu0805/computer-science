# 25. Matchings in Bipartite Graphs

## 25.1 Maximum bipartite matching

M-alternating path

M-augmenting path

symmetric difference

```
Hopcroft-Karp(G)
M = {}
repeat
    let P = {P_1, ..., P_k} be a maximal set of vertex disjoint shortes M-augmenting paths
    M = M SYMMETRIC DIFFERENCE(P_1 U P_2 U ... P_k)
until P == {}
return M
```
$O(\sqrt{V}E)$

### Exercises
25.1-1
25.1-2
25.1-3
25.1-4
25.1-5
25.1-6

## 25.2 The stable-marraige problem

complete bipartite grpah

```
Gale-Shapley(men, women, rankings)
assign each woman and man as free
while some woman w is free
    let m be the first man on w's ranked list to whom she has not proposed
    if m is free
        w and m engaged
    elif m ranks w higher tha currently engaged w'
        m breaks engagement with w`
        w abd n engaged
    else
        m rejects w
        w remains free

return matching
```

### Exercises
25.2-1
25.1-2
25.1-3
25.1-4
25.1-5

## 25.3 The Hungarian algorithm for the assignment problem

default vertex labeling

feasible vertex labeling

equality subgraph

directed equality subgraph

### Exercises
25.3-1
25.3-2
25.3-3
25.3-4
25.3-5
25.3-6
25.3-7

## Problems
25-1
25-2
25-3
25-4
25-5
