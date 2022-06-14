https://leetcode.com/problems/combination-sum/

```
class Solution:

    # Distinct candidates, unique solution, infinite uses
    # Test Case: [2, 3, 6, 7], 7    

    # Recursion Tree 
    # combinationSum(7) = [2 + combinationSum(7 - 2)] + [3 + combinationSum(7 - 3)] + [6 + combinationSum(7 - 6)] + [7 + combinationSum(7 - 7)] 
    # Repetitive when combinationSum(t) is already computed --> memoization
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution 1

        memo = [[] for _ in range(target + 1)]
        
        for t in range(target + 1):
            
            for c in candidates:
                
                if t < c:
                    continue
                
                elif t == c:
                    memo[t].append([c])
                    
                else:
                    for p in memo[t - c]:
                        if p[-1] <= c: # [2, 2, 3] is good, [2, 3, 2] is not
                            memo[t].append(p + [c])
                        
        return memo[-1]

        # Solution 2
        # Solve combinationSum with smaller set of candidates

        memo = [[] for _ in range(target + 1)]
        
        for c in candidates:
            
            for t in range(c, target + 1):
                
                if t == c:
                    memo[t].append([c])
                    
                else:
                    for p in memo[t - c]:
                        memo[t].append([c] + p)
                        
        return memo[-1]
```

https://leetcode.com/problems/combination-sum-ii/

```
class Solution:

    # Test Case: [10,1,2,7,6,1,5], 8
    # Repetitive candidates, unique solution, single use

    # Recursion Tree 
    # combinationSum2(8) = [candidates[0] + combinationSum(8 - candidates[0])] + ...
    # combinations of using the first candidate, using the second candidate, ...
    # No repetition in recursion tree due to indices instead of values
    # Unique solution needs to check use of the same value, [1, 7], [7, 1]
    # Straightforward way is store sorted tuples
    # Common algorithm is to sort and check whether the value has been used
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combinations = []
        path = []
        
        candidates.sort() # [1,1,2,5,6,7,10]
        self.backtrack(candidates, target, 0, path, combinations)
        return combinations
    
    def backtrack(self, candidates, target, i, path, combinations):
        
        if not target:
            combinations.append(path.copy())
            return
        
        if target < 0:
            return 
        
        for j in range(i, len(candidates)):
            
            if j > i and candidates[j] == candidates[j - 1]: # If combination using this value has already been backtracked
                continue
                
            path.append(candidates[j])
            self.backtrack(candidates, target - candidates[j], j + 1, path, combinations)
            path.pop()
            
        return

```