# 19. Data Structures for Disjoint Sets

## 19.1 Disjoint-set operations

-   Make-Set
-   Union
-   Find-Set
-   Connected Components

### Exercises

19.1-1
19.1-2
19.1-3

## 19.2 Linked-list representation of disjoint sets

-   The Union operation is where this implementation pays the price for Find-Set taking constant time: Union must also update the pointer to the set object for each object originally on y's list
-   Weighted union heuristic: always append the shorter to the longer

19.2-1
19.2-2
19.2-3
19.2-4
19.2-5

## 19.3 Disjoint-set forests

-   Union by rank
    -   during union compare ranks, which is bounded by the height of the tree,
    -   if the ranks are equal, choose one as teh parent and increase its rank
    -   if the ranks are unequal, make the higher one the parent of the lower one, but dont increase its rank

-   Path compression
    -   does not change ranks
    -   recursively two pass: first pass is find the root, second is to update the nodes in the path

19.3-1
19.3-2
19.3-3
19.3-4
19.3-5
