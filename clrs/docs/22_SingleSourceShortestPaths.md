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
