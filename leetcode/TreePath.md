Tree path problems usually involve returning the following,
1. Continuing the left path
2. Continuing the right path
3. Combining the left and right path

Typically, recursion is used to solve tree problems.
Therefore try to draw the tree and try to start from the leaf nodes to figure out the conditions.
Sometimes, simplifying the problem to 1D helps to find the logic.

https://leetcode.com/problems/diameter-of-binary-tree/

```
class Solution:

    # 1D problem increments from previous length
    # 2D needs to consider both child    
    # Left and right path can continue to grow when including current node, but only need the maximum
    # max(left_path + 1, right_path + 1)
    # Also need to keep track of left + right since path does not need to include root
    # left_path + right_path (edges), left_path + right_path +1 (nodes)
    # Therefore, need to memoize longest path seen so far, and longest path if continue to grow

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.max_path(root)[0]
    
    def max_path(self, node):        
        
        if not node:
            return 0, 0
        
        left_max, left_run = self.max_path(node.left)
        right_max, right_run = self.max_path(node.right)
        
        max_path = max(left_max, right_max, left_run + right_run)
        run_path = max(left_run, right_run) + 1
        
        return max_path, run_path
```

https://leetcode.com/problems/binary-tree-maximum-path-sum/

```
class Solution:

    # 1D problem is maximum subarray

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        return self.max_path_sum(root)[1]
    
    def max_path_sum(self, node):
        
        if not node:
            
            return 0, -float("inf")
        
        left_run, left_max = self.max_path_sum(node.left)
        right_run, right_max = self.max_path_sum(node.right)
        
        max_sum = max(left_max, right_max, left_run + right_run + node.val)
        run_sum = max(left_run, right_run) + node.val
        run_sum = max(run_sum, 0)
        
        return run_sum, max_sum
```

https://leetcode.com/problems/balanced-binary-tree/

```
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.balanced_tree(root)[0]    
    
    def balanced_tree(self, node):
    
        if not node:
            return True, 0
        
        left_balanced, left_height = self.balanced_tree(node.left)
        right_balanced, right_height = self.balanced_tree(node.right)
        
        balanced = abs(left_height - right_height) <= 1
        balanced &= left_balanced
        balanced &= right_balanced
        
        return balanced, 1 + max(left_height, right_height)
```