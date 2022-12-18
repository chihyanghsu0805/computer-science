"""Contain data structures."""

__all__ = ["BinarySearchTree", "BinarySearchTreeNode"]


class BinarySearchTreeNode:
    """Class for instance of binary search tree node."""

    def __init__(self, key: any, satellite: any = None) -> None:
        """Initialize class.

        Args:
            key (any): key for node.
            satellite (any, optional): satellite for node. Defaults to None.
        """
        self.key = key
        self.satellite = satellite
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class for instance of binary search tree."""

    def __init__(self) -> None:
        """Initialize class."""
        self.root = None

    def tree_insert(self, z: BinarySearchTreeNode) -> None:
        """Insert node into tree.

        Args:
            z (BinarySearchTreeNode): node to be inserted.
        """
        x = self.root
        y = None
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z

        elif z.key < y.key:
            y.left = z

        else:
            y.right = z

    def tree_search(self, k: any) -> BinarySearchTreeNode:
        """Search node with key in tree.

        Args:
            k (any): key.

        Returns:
            BinarySearchTreeNode: node with key.
        """
        x = self.root
        if x.key == k:
            return x

        while x and x.key != k:
            if x.key > k:
                x = x.left
            else:
                x = x.right

        return x

    def tree_minimum(self, x: BinarySearchTreeNode) -> BinarySearchTreeNode:
        """Find node with minimum key in tree rooted at x.

        Args:
            x (BinarySearchTreeNode): root of tree/subtree.

        Returns:
            BinarySearchTreeNode: node with minimum key.
        """
        while x.left:
            x = x.left

        return x

    def tree_maximum(self, x: BinarySearchTreeNode) -> BinarySearchTreeNode:
        """Find node with maximum key in tree rooted at x.

        Args:
            x (BinarySearchTreeNode): root of tree/subtree.

        Returns:
            BinarySearchTreeNode: node with maximum key.
        """
        while x.right:
            x = x.right

        return x

    def tree_successor(self, x: BinarySearchTreeNode) -> BinarySearchTreeNode:
        """Find successor of node.

        Args:
            x (BinarySearchTreeNode): node to find successor for.

        Returns:
            BinarySearchTreeNode: successor node.
        """
        if x.right:
            return self.tree_minimum(x.right)

        y = x.parent

        while y and x == y.right:
            x = y
            y = y.parent

        return y

    def tree_predecessor(self, x: BinarySearchTreeNode) -> BinarySearchTreeNode:
        """Find predecessor for node.

        Args:
            x (BinarySearchTreeNode): node to find predecessor for.

        Returns:
            BinarySearchTreeNode: predecessor node.
        """
        if x.left:
            return self.tree_maximum(x.left)

        y = x.parent

        while y and x == y.left:
            x = y
            y = y.parent

        return y

    def tree_delete(self, x: BinarySearchTreeNode) -> None:
        """Delete node from tree.

        Args:
            x (BinarySearchTreeNode): node to delete.
        """
        if not x.left:
            self.transplant(x, x.right)

        elif not x.right:
            self.transplant(x, x.left)

        else:
            # find successor y, by successor definition y have no left child
            y = self.tree_minimum(x.right)

            # if y is not immediate child of x, need to transplant y
            # connect y.parent with y.right, because y have no left child
            if y != x.right:
                self.transplant(y, y.right)
                y.right = x.right
                y.right.parent = y

            # connecet x.parent and x.left with y
            self.transplant(x, y)
            y.left = x.left
            y.left.parent = y

    def transplant(self, u: BinarySearchTreeNode, v: BinarySearchTreeNode) -> None:
        """Connect u.parent with v.

        Args:
            u (BinarySearchTreeNode): old child node.
            v (BinarySearchTreeNode): new child node.
        """
        if not u.parent:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        if v:
            v.parent = u.parent
