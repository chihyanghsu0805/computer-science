https://leetcode.com/problems/subarray-sum-equals-k/

```
class Solution:
    # O(N^2) brute force is use nested for loops.
    # Sliding window only works for non-negative numbers    
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        memo = {} # key: prefix_sum, value: count
        memo[0] = 1 # edge case
        prefix_sum = 0
        count = 0
        
        for n in nums:
            
            prefix_sum += n
            
            if prefix_sum - k in memo:
                # k - prefix_sum does not work
                # current = previous + k
                # previous = current - k
                count += memo[prefix_sum - k]
                
            memo[prefix_sum] = memo.get(prefix_sum, 0) + 1
            
        return count
```