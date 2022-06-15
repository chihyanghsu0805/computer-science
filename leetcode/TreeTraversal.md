https://leetcode.com/problems/path-sum/

```
class Solution:
    # DFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
            
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
```

https://leetcode.com/problems/path-sum-ii/

```
class Solution:
    # BFS
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        queue = deque()        
        queue.append([root, targetSum, []])
        
        paths = []
        
        while queue:
            
            node, target, path = queue.popleft()
            
            if node:
                if not node.left and not node.right and node.val == target:
                    paths.append(path + [node.val])
                
                queue.append([node.left, target - node.val, path + [node.val]])
                queue.append([node.right, target - node.val, path + [node.val]])
                    
        return paths
```

https://leetcode.com/problems/find-duplicate-subtrees/

```
def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        memo = {}
        self.preorder(root, memo)
        
        return [v[0] for v in memo.values() if len(v) > 1]
    
    def preorder(self, node, memo):
        
        if not node:
            return "#"
        
        path = []
        path.append(str(node.val))
        path.append(self.preorder(node.left, memo))
        path.append(self.preorder(node.right, memo))
        
        path_str = "^".join(path)
        if path_str not in memo:
            memo[path_str] = []
            
        memo[path_str].append(node)
        return path_str
```
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

```
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        root_index = inorder.index(root.val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        
        left_preorder = preorder[1:root_index + 1]
        right_preorder = preorder[root_index + 1:]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
```