# 17. Augmenting Data Structures

## 17.1 Dynamic order statistics

Order statistic tree is a red-black tree with x.size indicating number of internal nodes in its subtree

x.size = x.left.size + x.right.size + 1

Rank is the position a node would be printed in an inorder since keys dont need to be unique

OS-Select: O(lg n)

OS-Rank: O(lg n)

Maintaining size O(lg n)

-   Insertion: increment size for each node on the path, correct when rotated
-   Deletion: traverse from the lowest to the root and decrease size

### Exercises

17.1-1
17.1-2
17.1-3
17.1-4
17.1-5
17.1-6
17.1-7
17.1-8

## 17.2 How to augment a data structure

1.  Choose an underlying data structure
2.  Determine additional information to maintain
3.  Verify the information can be maintained with basic operations
4.  Develop new operations

### Exercises

17.2-1
17.2-2
17.2-3

## 17.3 Interval trees

Interval tree is a red-black tree containing an interval x.int
-   key of x is the low endpoint x.int.low
-   also has x.max which is the max endpoint in the subtree rooted at x
-   x.max = max{x.int.high, x.left.max, x.right.max}

Interval-Search O(lg n)

### Exercises

17.3-1
17.3-2
17.3-3
17.3-4
17.3-5
17.3-6

## Problems

17-1
17-2
