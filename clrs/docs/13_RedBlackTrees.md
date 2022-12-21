# 13. Red Black Trees

Binary search trees support basic dynamic-set operations in O(h) time, which could be O(N) in worst case.
Red black trees are `balanced` search trees to guarantee O(lgN) for basic dynamic-set operations.

## 13.1 Properties of red-black trees

Extra bit of storage per node for the color, `RED` or `BLACK`, for constraining paths to be no longer then twice of others.

Height of red-black tree with N keys is at most 2lg(N+1) --> O(lgN) for basic dynamic-set operations.

`Red-Black properties`:
1.  Every node is either `RED` or `BLACK`
2.  Root is `BLACK`
3.  Leaf is `BLACK`
4.  If node is red, both children are `BLACK`
5.  For each node, all simple paths from node to descendant leaves have same number of `BLACK` nodes

Black height bh(x) is the number of `BLACK` nodes on any simple path rooted from x, but not including x.

## Exercises

13.1-8 `RED` nodes must have `BLACK` children, if one is NIL then bh is one, but if the other child is not NIL, the bh must be 2 (itself and NIL). Therefore violates property 5.

## 13.2 Rotations

Tree-Insert and Tree-Delete may violate red-black tree properties, therfore `colors` and `pointers` need to be changed.

Pointers are changed with [left rotation] and [right rotation].

## Exercises

13.2-1 [Right Rotation]
13.2-3 depth of a + 1, depth of b + 0, depth of c - 1

## 13.3 Insertions

Insert a node, color `RED`, fix the color.

Which properties are violated:

1.  Every node is either `RED` or `BLACK`
-   NOT violated because new node is `RED`
2.  Root is `BLACK`
-   May be violated if new node is root
3.  Leaf is `BLACK`
-   NOT violated because new node's children are NIL which is `BLACK`
4.  If node is `RED`, both children are `BLACK`
-   May be violated if new node's parent is `RED`
5.  For each node, all simple paths from node to descendant leaves have same number of `BLACK` nodes
-   NOT violated because new node replaced a leaf which is `BLACK` but added two more leaf nodes so bh is maintained

[Insertion]

## 13.3 Deletions