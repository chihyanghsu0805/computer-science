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

Which properties are violated?

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

Insert takes O(lgN), RB-FixUp only repeats in Case 1 at most logN times and no more than two rotations in Case 2 and 3, so O(lgN), overall, O(lgN).

13.3-1 Because it would be adding bh unconditionally and might violate 5.
13.3-4 RB-FixUp only marks z.parent.parent RED. For NIL to be z.parent.parent, z.parent must be root whick is BLACK violates while loop condition. Root may be colored RED but would be corrected in the last color assignment.
13.3-5 Using RB-Insert, at least z is RED. IN RB-Insert-FixUp, if while loop ix executed, tehn at least z.parent is RED. The only exception is z is root.

## 13.4 Deletions

Find replacement (y), transplant, if y was `BLACK` fix the color.

Which properties are violated?

1.  Every node is either `RED` or `BLACK`
-   Violated due to fix of 5
2.  Root is `BLACK`
-   May be violated if root is deleted and replacement is `RED`
3.  Leaf is `BLACK`
-   NOT violated
4.  If node is `RED`, both children are `BLACK`
-   May be violated if y.parent was `RED` and y's transplant is `RED`
5.  For each node, all simple paths from node to descendant leaves have same number of `BLACK` nodes
-   Originally violated if y was `BLACK` for all y's ancestor, fix with additional `BLACK`

FixUp seeks consumption of the addtional `BLACK` through  transfer up or sibling's children.

[Deletion]

Delete takes O(lgN), FixUp transfer up takes at most O(logN), sibling's children takes constant.
