# 14. Dynamic Programming

Optimal substructure exists, and subproblems overlap, .

1.  Characterize the structure of an optimal solution
2.  Recursively define the value of an optimal solution
3.  Compute the value of an optimal solution, typically in a bottom up fashion
4.  (optional) Construct an optimal solution (choice) from computed information

## 14.1 Rod cutting

Given a rod with length n, and different price for different lengths, find maximum revenue

2<sup>n-1</sup> ways to cut a rod, cut or not for each unit

1.  Optimal structure:
-   Denote i as i inch from left, optimal solution cuts the rod in k pieces, 1 <= k <= n
-   n = i<sub>1</sub> + ... + i<sub>k</sub>

2.  Recursive solution
-   r<sub>n</sub> = max{p<sub>n</sub>, r<sub>1</sub> + r<sub>n - 1</sub>, ..., r<sub>n - 1</sub> + r<sub>1</sub>}
-   p<sub>n</sub> is no cut
-   Subproblem is the maximum revenue of the two pieces (r<sub>i</sub>, r<sub>n-i</sub>)
-   If the left piece can not be divided, r<sub>n</sub> = max{p<sub>i</sub> + r<sub>n - i</sub> : 1 <= i <= n}

3.  Compute value

[Recursive solution](../scripts/ch14.py)

Total number of calls $T(n) = 1 + \sum_{j=0}^{n-1} T(j) = 2^n, T(0) = 1$

[Dynamic Programming solution](../scripts/ch14.py)

4.  [Construct solution](../scripts/ch14.py)

$\Theta(2^n) -> \Theta(n^2)$

-   Time-memory trade-off
-   In some special cases, top down does not actually recurse all possible subproblems
-   Bottom up often has better constant
-   `Subproblem graphs`, directed graph as a reduced / collapsed version of the recursion tree
-   Bottom up solves in reverse topological sort

### Exercises
14.1-1
14.1-2
14.1-3 Add -c to each recursive call
14.1-4 Needto add the revenue of the other piece. Not changed?
14.1-5 Add s
14.1-6

## 14.2 Matrix chain multiplication

Find optimal parenthese for minimal operations to multiply matrices.

if n = 1, $P(n) = 1$

if n >= 2, $P(n) = \sum_{k=1}^{n-1} P(k)P(n-k)$

1.  Optimal structure:
-   For matrices A<sub>i</sub> ... A<sub>j</sub>, find (A<sub>i</sub> ... A<sub>k</sub>) x (A<sub>k+1</sub> ... A<sub>j</sub>) with minimal operations.
-   Try all k.

2.  Recursive solution
-   if i = j, m[i, j] = 0
-   if i < j, min{m[i, k] + m[k + 1, j] + p<sub>i-1</sub>p<sub>k</sub>p<sub>j</sub> : i <= k < j}

3. [Compute value](../scripts/ch14.py)

3. [Construct solution](../scripts/ch14.py)

$\Omega(2^n) -> \Theta(n^3)$

### Exercises
14.2-1
14.2-2
14.2-3
14.2-4
14.2-5
14.2-6

## 14.3 Elements of dynamic programming

-   Optimal substructure
    -   Running time depends on number of subproblems and number of choices for each
    -   Independent subproblems

-   Overlapping subproblems

### Exercises
14.3-1
14.3-2
14.3-3
14.3-4
14.3-5

## 14.4 Longest common subsequence

Find Z, the LCS of X and Y

1.  Optimal substructure
-   If X<sub>m</sub> = Y<sub>n</sub>, Z<sub>k - 1</sub> is LCS of X<sub>m - 1</sub> and Y<sub>n - 1</sub>
-   If X<sub>m</sub> != Y<sub>n</sub>
    -   Z<sub>k</sub> != X<sub>m</sub> Z<sub>k - 1</sub> is LCS of X<sub>m - 1</sub> and Y<sub>n</sub>
    -   Z<sub>k</sub> != Y<sub>n</sub> Z<sub>k - 1</sub> is LCS of X<sub>m</sub> and Y<sub>n - 1</sub>
2.  Recursive solution

-   if i = 0 or j = 0, c[i, j] = 0
-   if i, j > 0 and x<sub>i</sub> = y<sub>j</sub>, c[i, j] = c[i - 1, j - 1] + 1
-   if i, j > 0 and x<sub>i</sub> != y<sub>j</sub>, c[i, j] = max(c[i - 1, j], c[i, j - 1]]
-   Improving the code

$\Omega(mn)$

### Exercises
14.4-1
14.4-2
14.4-3
14.4-4 compute i % 2, overwrite
14.4-5 https://leetcode.com/problems/longest-increasing-subsequence/
14.4-6 https://leetcode.com/problems/longest-increasing-subsequence/
