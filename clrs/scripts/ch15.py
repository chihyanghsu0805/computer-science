"""Contain implementation for ch15."""

from heapq import heappop, heappush
from typing import List, Tuple

START = [0, 1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
END = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

C = [(5, "F"), (9, "E"), (12, "C"), (13, "B"), (16, "D"), (45, "A")]


class Node:
    """Construct class for Node with key and frequency."""

    def __init__(self, freq: int, key: str):
        """Initialize the class.

        Args:
            freq (int): frequncy of character.
            key (str): character.
        """
        self.f = freq
        self.k = key
        self.left = None
        self.right = None


def recursive_activity_selector(s: List, f: List, k: int, n: int) -> List:
    """Solve maximum activity selection recursively.

    Args:
        s (List): list of start times.
        f (List): list of finish times.
        k (int): start index.
        n (int): number of activities.

    Returns:
        List: list with activity indices.
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1

    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)

    else:
        return []


def greedy_activity_selector(s: List, f: List, n: int) -> List:
    """Solve maximum activity selection greedy.

    Args:
        s (List): list of start times.
        f (List): list of finish times.
        n (int): number of activities.

    Returns:
        List: list with activity indices.
    """
    A = [1]
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A = A + [m]
            k = m

    return A


def huffman(C: List[Tuple[int, str]]) -> Tuple[int, Node]:
    """Perform huffman coding.

    Args:
        C (List[Tuple[int, str]]): characters with frequency.

    Returns:
        Tuple[int, Node]: tuple of frequency and node.
    """
    n = len(C)
    q = []

    for f, k in C:
        heappush(q, (f, Node(f, k)))

    for _ in range(n - 1):
        x_f, x = heappop(q)
        y_f, y = heappop(q)
        z = Node(x.f + y.f, "")
        z.left = x
        z.right = y
        heappush(q, (z.f, z))

    return heappop(q)


def inorder(node: Node) -> None:
    """Traverse inorder.

    Args:
        node (Node): node with key and frequency.
    """
    if not node:
        return

    inorder(node.left)
    print(f"{node.k}: {node.f}")
    inorder(node.right)

    return


if __name__ == "__main__":

    a = recursive_activity_selector(START, END, 0, len(START) - 1)
    print(a)
    a = greedy_activity_selector(START, END, len(START) - 1)
    print(a)

    _, root = huffman(C)
    inorder(root)
