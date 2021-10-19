# Algorithms
https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/

## Graph
- BFS: Graph traversal and visit siblings first. Good for finding shortest path. O(V+E)
- DFS: Graph traversal and visit children first. Good for puzzles and games. O(V+E)
- Dijkstra: Finding shortest path (with distance) between nodes, does not work on negativ weights. O(V<sup>2</sup>), with binary heap O(ElogV)
- FloydWarshall: Finding shortest path (with distance) between all nodes. O(V<sup>3</sup>)
- Union-Find: Detect cycles in graph, assuming no self loops. O(N), can be improved to O(logN) or O(1).
- Prim: Find minimum spanning tree. O(V<sup>2</sup>)
- Kruskal: Find minimum spanning tree. O(ElogE) or O(ElogV)
- Topological Sort: Linear ordering of vertices do Directed Acyclic Graph (DAG) that parent always come before children. O(V+E)
- Boggle: Find words in Boggle board. DFS: O(MN8<sup>MN</sup>), Trie: O(8<sup>MN</sup>)
- Bridges: Find bridges in graph. O(V+E)

## Linked List
- Sorted Insertion: O(N)
- Delete Node: O(N)
- Compare String: O(N)
- Add Numbers (signifcant digits first): O(M+N)
- Merge ALternate: O(N)
- Reverse Groups: O(N)
- Intersection and Union: O(M+N)
- Detect and Remove Loop: O(N)
- Merge Sort: O(NlogN)
- Select Random (Reservoir Sampling): O(N)

## Dynamic Programming
- Longest Common Sequence: O<sub>T</sub>(MN), O<sub>S</sub>(MN) -> O<sub>S</sub>(N)
- Longest Increasing Subsequence: O(NlogN)
- Minimum Cost: O<sub>T</sub>(MN), O<sub>S</sub>(MN) -> O<sub>S</sub>(N)
- Minimum Partition Sum: O<sub>T</sub>(NS), O<sub>S</sub>(NS) -> O<sub>S</sub>(N)
- Number of Ways: O<sub>T</sub>(N), O<sub>S</sub>(N) -> O<sub>S</sub>(1)
- Longest Path: O<sub>T</sub>(MN), O<sub>S</sub>(MN)
- Subset Sum: O<sub>T</sub>(NS), O<sub>S</sub>(NS)
    - Find All Subset Sum: O<sub>T</sub>(NS), O<sub>S</sub>(NS)
- Coin Game: O<sub>T</sub>(N<sup>2</sup>), O<sub>S</sub>(N<sup>2</sup>)
- 0-1 Knapsack: O<sub>T</sub>(NW), O<sub>S</sub>(NW)
- Boolean Evaluation: O(N<sup>3</sup>)

## Sorting and Searching
- Binary Search: O(logN)
- Search in Sorted and Rotated: O(logN)
- Bubble Sort: O(N<sup>2</sup>)
- Insertion Sort: O(N<sup>2</sup>)
- Merge Sort: O(NlogN)
- Heap Sort: O(NlogN)
- Quick Sort: O(NlogN)
- Interpolation Search: O(N)
- Kth Smallest/Largest Element in Array: O(N) (expected)
- Find Pair with Closest Sum in Sorted Array: O(N)

## Tree
- Minimum Depth of Binary Tree: O(N)
- Maximum Path Sum: O(N)
- Check Array is Preorder of Binary Tree: O(N)
- Check Full Binary Tree: O(N)
- Bottom View: O(N)
- Top View: O(N)
- Remove Node with path < K: O(N)
- Lowest Common Ancestor: O(H)
- Subtree: O(N)
- Reverse Alternate Level: O(N)

## Number Theory
- Modular Exponentiation: O(logN)
- Modular Multiplicative Inverse: O(N) -> O(logN)
- Primality Test: O(N) -> O(N<sup>1/2</sup>) -> O(klogN)
- Euler's Totient: O(NlogN)
- Sieve of Eratosthenes (Count Primes): O<sub>T</sub>(NloglogN), O<sub>S</sub>(N)
- Convex Hull: O(N<sup>2</sup>)
- Euclidean Algorithms: O(log(min(A,B)))
- Segmented Sieve: O<sub>T</sub>(NloglogN), O<sub>S</sub>(N<sup>1/2</sup>)
- Remainder Theorem: O(N)
- Lucas Theorem: O(p<sup>2</sup>log<sub>p</sub>N)

## Bit
- Maximum Subarray XOR: O(N<sup>2</sup>) -> O(N)
- Nth Magic Number: O(1)
- Sum Bit Difference: O(N<sup>2</sup>) -> O(N)
- Swap Bits: O(1)
- Find Once: O(N)
- Binary Representation: O(1)
- Count Bits: O(1)
- Rotate Bits: O(1)
- Count Flip Bits: O(1)
- Find Next Sparse Number: O(logX)

## Strings and Arrays
- Reverse String Ignoring Special Character: O(N)
- All Possible Palindrome Partitions: O(N<sup>2</sup>)
- Count Triples with Smaller Sum: O(N<sup>2</sup>)
- Zig Zag: O(N)
- Generate All Sorted Subarray from Two Sorted Arrays:
- Pythagorean Triplets: O(N<sup>2</sup>)
- Find Smallest Positive Integer not a Sum: O(N)
- Length of Largest Subsequence: O(N<sup>2</sup>)
- Maximize Profit: O(N)
