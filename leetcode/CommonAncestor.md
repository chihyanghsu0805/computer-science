https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

```
class Solution:
    # Search subtree for p or q return p or q if found
    # if found p/q in left and found p/q in right, return root    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left or right
```

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

```
class Solution:

    # BST properties simplifies the problem
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
```
