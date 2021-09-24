# Algorithms
https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/

## Graph
- BFS: Graph traversal and vist siblings first. Good for finding shortest path. O(V+E)
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
