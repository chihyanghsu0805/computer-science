https://leetcode.com/problems/subsets/

```
class Solution:

    # Unique elements, unique solution, single use
    # Add every path
    # Find all path with i-th number
    # Recursion, use or no use for each element

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sets = []
        path = []
        
        self.backtrack(nums, 0, path, sets)
        return sets
    
    def backtrack(self, nums, i, path, sets):
        
        sets.append(path.copy()) # Add every path
        
        for j in range(i, len(nums)):
            path.append(nums[j])
            self.backtrack(nums, j + 1, path, sets)
            path.pop()
            
        return
```

https://leetcode.com/problems/subsets-ii/

```
class Solution:

    # Duplicate elements, unique solution, single use
    # Common algorithm is to sort and check whether the value has been used

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        path = []
        
        nums.sort()
        
        self.backtrack(nums, 0, path, subsets)
        
        return subsets
    
    def backtrack(self, nums, i, path, subsets):
        
        subsets.append(path.copy())
        
        for j in range(i, len(nums)):
            
            if j > i and nums[j] == nums[j - 1]:
                continue
                
            path.append(nums[j])
            self.backtrack(nums, j + 1, path, subsets)
            path.pop()
            
        return
```