For array problems, it is common to find / search elements.
After figuring out the logic, try optimize by binary search if possible.
Binary search works on sorted arraysm but sometimes the sorted property is implicit.

https://leetcode.com/problems/binary-search/

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binary_search(nums, target)
    
    def binary_search(self, arr, n):
        
        # Often search the array indices
        # Some problems search a custom range
        lo = 0
        hi = len(arr) - 1
        
        # There are many templates for binary search
        # All versions work equally, but differs due to sign and +- 1
        # Choose one and understand the conditions well

        while lo <= hi: # Version differ
            
            mid = lo + (hi - lo) // 2 # Prevent overflow
            
            # Typically compares three conditions
            if arr[mid] > n:
                hi = mid - 1
                
            elif arr[mid] < n:
                lo = mid + 1
                
            else:
                return mid
            
        return -1 # Different versions also may return different indices
```

https://leetcode.com/problems/koko-eating-bananas/

```
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        return self.binary_search(piles, h)
    
    def compute_time(self, piles, n):
        
        t = 0
        for p in piles:
            t += ceil(p / n)
            
        return t
    
    def binary_search(self, piles, h):
        
        # Minimum eat 1, maximum eat max(piles)
        lo = 1
        hi = max(piles)
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            # Sometimes comparison is not directly mid but a function of mid
            need = self.compute_time(piles, mid)
            
            # It helps to always explicitely right out the conditions to discuss the edge cases
            if need > h:
                lo = mid + 1
                
            elif need < h:
                hi = mid - 1
                
            else:
                hi = mid - 1
        
         # This version of binary search exits the while loop while lo > hi
         # Therefore, the lo is the smallest value satisfying the condition
         # Similar to bisect.bisect_left
         # In other words, [1, 3, 4] find bigger than 1, it returns [1, 2, 4]
        return lo
```
