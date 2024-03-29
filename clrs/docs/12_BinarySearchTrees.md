# 12. Binary Search Trees (BST)

## 12.1 What is a binary search tree?

Basic operations (SEARCH, MINIMUM, MAXIMUM, PREDECESSOR, SUCCESSOR, INSERT and DELETE) takes time proportional to height of tree, h.

For a complete tree, worst case time is $\theta$(lgN), for a linear chain, worst case time is $\theta$(N).

Expected height of BST is O(lgN).

In addition to a key and satellite data, each node contains attributes left, right, and parent.

The root is the only node with parent = NULL.

Binary search tree property: x.left.key <= x.key <= x.right.key

Keys can be printed in sorted order by [INORDER-TREE-WALK](./ch12.py#L6) in $\theta$(N) time.


## 12.2 Querying a binary search tree

[Searching](./data_structures.py#L54), O(h)

[Minimum](./data_structures.py#L75), O(h)

[Maximum](./data_structures.py#L89), O(h)

[Successor](./data_structures.py#L103), O(h)

[Predecessor](./data_structures.py#L123), O(h)

## 12.3 Insertion and deletion

[Insertion](./data_structures.py#L30), O(h)

[Deletion](./data_structures.py#L143), O(h)

## Problems

12.4 https://leetcode.com/problems/unique-binary-search-trees/
