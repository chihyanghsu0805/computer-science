"""Contain red black tree."""

from clrs.data_structures.binary_search_tree import BinarySearchTree
from clrs.data_structures.binary_tree import BinaryTreeNode

__all__ = ["RedBlackTree", "RedBlackTreeNode"]

RED = "R"
BLACK = "B"


class RedBlackTreeNode(BinaryTreeNode):
    """Class for instance of red black tree node."""

    def __init__(self, key: any, satellite: any = None) -> None:
        """Initialize class.

        Args:
            key (any): key for node.
            satellite (any, optional): satellite for node. Defaults to None.
        """
        super().__init__(key, satellite)
        self.color = RED
        # What is the best way to do this?
        # self.left = sentinel
        # self.right = sentinel


class RedBlackTree(BinarySearchTree):
    """Class for instance of red black tree."""

    def __init__(self) -> None:
        """Initialize class."""
        super().__init__()
        # NIL has color of black and arbitrary values for other attributes
        self.NIL = RedBlackTreeNode(-1)
        self.NIL.color = BLACK
        # Initial root should be NIL
        self.root = self.NIL

    def tree_insert(self, z: RedBlackTreeNode) -> None:
        """Insert node into tree.

        Args:
            z (RedBlackTreeNode): node to be inserted.
        """
        z.parent = self.NIL
        z.left = self.NIL
        z.right = self.NIL

        x = self.root
        y = self.NIL

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.NIL:
            self.root = z

        elif z.key < y.key:
            y.left = z

        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = RED

        self.tree_insert_fixup(z)

        return

    def tree_insert_fixup(self, z: RedBlackTreeNode) -> None:
        """Fix colors and pointers to maintain red black tree properties.

        Args:
            z (RedBlackTreeNode): a red black tree node.
        """
        # Loop invariant
        # (a) z is RED
        # (b) if z.parent is root, z.parent is BLACK
        # (c) if tree violates the properties, it violates AT MOST one of them
        # (property 2 or property 4)

        # Initialization
        # (a) z is RED
        # (b) root (NIL) is BLACK, z.parent is NIL
        # (c) if property 2 is violated then since z is RED with z.parent (NIL)
        # and z.left (NIL) and z.right (NIL) is BLACK so property 4 is not
        # violated. If 4 is violated, z and z.parent are RED so z and z.parent
        # are not root, and root is BLACK

        while z.parent.color == RED:
            # Maintenance
            # (a) z is RED
            # (b) z.parent is NIL and NIL is BLACK
            # (c) property 4 is violated since z and z.parent are both RED

            if z.parent == z.parent.parent.left:

                y = z.parent.parent.right  # z.uncle

                if y.color == RED:
                    # Case 1: z.uncle is RED and z.parent is RED
                    # Transfer BLACK from z.parent.parent down to
                    # z.parent and z.uncle, bh is not violated
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    # z.parent.parent may be root, so this may violate property
                    # 2 but property 4 is maintained since z.parent and z.uncle
                    # (y) are now RED
                    z = z.parent.parent

                else:
                    # Case 2: z.uncle is BLACK and z is a right child
                    if z == z.parent.right:
                        z = z.parent
                        # Left rotate makes z the parent and z.parent the left
                        # child then apply Case 3
                        self.left_rotate(z)

                    # Case 3: z.uncle is BLACK and z is a left child
                    z.parent.color = BLACK
                    # Maintains 4, but bh + 1
                    z.parent.parent.color = RED
                    # z.parent.parent may be root, so this may violate property
                    # 2
                    self.right_rotate(z.parent.parent)
                    # Right rotate to keep bh

                # If z.uncle z.parent are RED, transfer BLACK down
                # Otherwise mark parent BLACK and ROTATE to keep bh (property 5)

            else:
                # Symmetric
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        # Termination
        # If only Case 1 occurs, pointer is not changed, color is changed but bh
        # is maintained, and z.parent eventuall becomes root and is BLACK
        # If Case 2 or Case 3, the loop terminates when z.parent is BLACK which
        # maintains property 4

        # Maintains property 2
        self.root.color = BLACK

        return

    def left_rotate(self, x: RedBlackTreeNode) -> None:
        """Rotate left, right child becomes parent, parent becomes left child.

        Args:
            x (RedBlackTreeNode): a red black tree node.
        """
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.NIL:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        return

    def right_rotate(self, x: RedBlackTreeNode) -> None:
        """Rotate right, left child becomes parent, parent becomes right child.

        Args:
            x (RedBlackTreeNode): a red black tree node.
        """
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.NIL:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        return
