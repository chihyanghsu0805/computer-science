# 14. Dynamic Programming

When subproblems overlap.

1.  Characterize the structure of an optimal solution
2.  Recursively define the value of an optimal solution
3.  Compute the value of an optimal solution, typically in a bottom up fashion
4.  (optional) Construct an optimal solution (choice) from computed information

## 14.1 Rod cutting

Given a rod with length n, and different price for different lengths, find maximum revenue

2<sup>n-1</sup> ways to cut a rod, cut or not for each unit

Denote i as i inch from left, optimal solution cuts the rod in k pieces, 1 <= k <= n

n = i<sub>1</sub> + ... + i<sub>k</sub>

r<sub>n</sub> = max{p<sub>n</sub>, r<sub>1</sub> + r<sub>n - 1</sub>, ..., r<sub>n - 1</sub> + r<sub>1</sub>}

p<sub>n</sub> is no cut

Subproblem is the maximum revenue of the two pieces (r<sub>i</sub>, r<sub>n-i</sub>)

If the left piece can not be divided, r<sub>n</sub> = max{p<sub>i</sub> + r<sub>n - i</sub> : 1 <= i <= n}

[Recursive solution]

Total number of calls $T(n) = 1 + \sum_{j=0}^{n-1} T(j) = 2^n, T(0) = 1$


[Dynamic Programming solution]

$\theta(n^2)$

Time-memory trade-off

In some special cases, top down does not actually recurse

Bottom up often has better constant

Subproblem graphs, directed graph as a reduced / collapsed version of the recursion tree

Bottom up solves in reverse topological sort

### Exercises
14.1-3 Add - c to each recursive call
14.1-4 Needto add the revenue of the other piece. Not changed?
14.1-5 Add s
