# 12. Binary Search Trees (BST)

## 12.1

Basic operations (SEARCH, MINIMUM, MAXIMUM, PREDECESSOR, SUCCESSOR, INSERT and DELETE) takes time proportional to height of tree, h.

For a complete tree, worst case time is $\theta$(lgN), for a linear chain, worst case time is $\theta$(N).

Expected height of BST is O(lgN).

In addition to a key and satellite data, each node contains attributes left, right, and parent.

The root is the only node with parent = NULL.

Binary search tree property: x.left.key <= x.key <= x.right.key

Keys can be printed in sorted order by [INORDER-TREE-WALK]([./ms/ch12.py](https://github.com/chihyanghsu0805/computer-science/blob/3a2c3d60a71c603b95242ff57f3cae6a9b964738/clrs/ch12.py#L6)) in $\theta$(N) time.


## 12.2

[Searching](./tree_search.py), O(h)

Minimum, O(h)

Maximum, O(h)

Successor, O(h)

Predecessor, O(h)

## 12.3

[Insertion](./data_structures.py), O(h)

Deletion, O(h)

## Problems

12.4 https://leetcode.com/problems/unique-binary-search-trees/
