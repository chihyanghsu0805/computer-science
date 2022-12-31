# 18. B-Trees

B-trees may have many children, that is branching factor may be large

N node B-trees have height logN

Internal node contains x.n keys with x.n + 1 children

Root is always in main memory

## 18.1 Definitions of B-trees


B-tree has the following properties:

1.  Each node x has the following attributes

    a.  x.n number of keys
    b.  the keys themselves
    c.  x.leaf boolean to indicate whether x in a leaf node

2.  Each internal node contains x.n + 1 pointers to its children, x.c<sub>i</sub>. Leaf node has no children, so undefined

3.  The keys separate the ranges of keys in the subtrees

4.  All leaves hae the same depth

5.  Nodes have lower and upper bound on the number of keys, t>= 2 the minimum degree

    a.  Every non-root node must have at lesast t - 1 keys, internal nodes thus have at least t children
    b.  Every node conatins at mode 2t - 1 keys (full), internal nodes thus have at most 2t children

B<sup>+</sup>-tree stores all satellite information in leaves

### Exercises

18.1-1
18.1-2
18.1-3
18.1-4
18.1-5

## 18.2 Basic Operations on B-trees

Searching, O(tlogn)

Creating,

Inserting into existing leaf node, if full, split around median. To avoid going back up the tree, split every full node when going down. O(tlogn)

### Exercises

18.2-1
18.2-2
18.2-3
18.2-4
18.2-5
18.2-6
18.2-7

## 18.3 Deleting a key from a B-tree

-   Case 1: Search arrives at lef node x, if x contains k, delete

-   Case 2: Search arrives at an interal node x containing k

    -   a: x.c<sub>i</sub> has at least t keys, find predecessor k', recursively delete k, and replace k with k'
    -   b: x.c<sub>i + 1</sub> has t - 1 keys, find successor k', recursively delete k, and replace k with k'
    -   c: both x.c<sub>i</sub> and x.c<sub>i + 1</sub> has t - 1 keys, merge x.c<sub>i</sub> and x.c<sub>i + 1</sub> and remove k

-   Case 3: Search arrives at an interal node x not containing k, continuse searching while ensurin gvisited nodes has at least t keys

    -   a: x.c<sub>i</sub> has t - 1 but has sibling with at least t, move a key from sibling to x and move appropraite to x.c<sub>i</sub>
    -   b: x.c<sub>i</sub> and siblings has t - 1, merge with a sibling

O(tlogn)

### Exercises

18.3-1
18.3-2

## Problems

18-1
18-2
