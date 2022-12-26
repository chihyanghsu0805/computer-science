# 15. Greedy Algorithms

Locally optimal solution leads to globally optimal solution.

## 15.1 An activity-selection problem

-   Optimal substructure: A<sub>ij</sub>> must include  optimal solutions to the two subproblems S<sub>ik</sub> and S<sub>kj</sub>

-   Making the greedy choice:
    -   If a<sub>m</sub> is the activity with earliest finish time, it should be included / compatible with the current selection
    -   Left with one subproblem
-   [Recursive greedy algorithm](../scripts/ch15.py)
-   [Iterative greedy algorithm](../scripts/ch15.py)

### Exercises

15.1-1
15.1-2
15.1-3
-   Minimum duration may not be the best option in cases like [10, 20], [19, 22], [21, 30]
-
-   Earliest start time may not be the best option in cases like [1, 100], [2, 3], [4, 5]
15-1.4 https://leetcode.com/problems/meeting-rooms-ii/
15.1-5 https://leetcode.com/problems/maximum-profit-in-job-scheduling/

## 15.2 Elements of the greedy strategy

-   Greedy choice property: make a choice before solving the subproblems
-   Optimal substructure: prove the choice is globally optimal
-   Greedy versus dynamic programming: greedy for fractional knapsack, dp for 0-1 knapsack

### Exercises

15.2-1
15.2-2 https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
15.2-3
15.2-4
15.2-5 Convex Hull
15.2-6
15.2-7

## 15.3 Huffman codes

Compression by using variable length code over fixed length code

-   Prefix-free codes can always achieve the optimal data compression
-   Constructing a Huffman code: greedily merge the two least frequent leaf nodes
-   Greedy choice property: minimum cost can be achieved by merging two least frequent character
-   Optimal substructure: tree T with least frequent leaf nodes x, y must be optimal

### Exercises

15.3-1
15.3-2
15.3-3
15.3-4
15.3-5
15.3-6
15.3-7
15.3-8
