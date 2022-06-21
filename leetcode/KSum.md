https://leetcode.com/problems/two-sum/
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        memo = {}
        
        for i, n in enumerate(nums):
            
            if target - n in memo:
                return [memo[target - n], i]
            
            memo[n] = i
```

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            if numbers[left] + numbers[right] > target:
                right -= 1
                
            elif numbers[left] + numbers[right] < target:
                left += 1
                
            else:
                return [left + 1, right + 1]                
```

https://leetcode.com/problems/3sum/
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        triplets = []
        
        for i, n in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            pairs = self.two_sum(nums, i + 1, 0 - n)
            
            for p in pairs:
                triplets.append([n] + p)
                
        return triplets
    
    def two_sum(self, nums, start, target):
        
        j = start
        k = len(nums) - 1        
        
        pairs = []
        
        while j < k:
            
            if (nums[j] + nums[k] > target) or (k < len(nums) - 1  and nums[k] == nums[k + 1]):
                k -= 1
                
            elif (nums[j] + nums[k] < target) or (j > start and nums[j] == nums[j - 1]):
                j += 1
                
            else:
                pairs.append([nums[j], nums[k]])
                j += 1
                k -= 1
                
        return pairs               
```

https://leetcode.com/problems/4sum/
```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        return self.k_sum(nums, target, 4, 0)
    
    def two_sum(self, nums, target, start):
        
        pairs = []
        
        left = start
        right = len(nums) - 1
        
        while left < right:
            
            if (nums[left] + nums[right] > target) or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                right -= 1
                
            elif (nums[left] + nums[right] < target) or (left > start and nums[left] == nums[left - 1]):
                left += 1
                
            else:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
                
        return pairs
    
    def k_sum(self, nums, target, k, start):
        
        if k == 2:
            return self.two_sum(nums, target, start)
        
        k_let = []
        for i in range(start, len(nums)):
            
            n = nums[i]
            
            if i > start and n == nums[i - 1]:
                continue
                
            temp = self.k_sum(nums, target - n, k - 1, i + 1)
            
            for t in temp:
                k_let.append([n] + t)
                
        return k_let
```

https://leetcode.com/problems/3sum-closest/ (TLE)
```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        min_diff = float("inf")
        min_sum = 0
        
        for i, n in enumerate(nums):
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                
                total = nums[i] + nums[j] + nums[k]
                
                if abs(target - total) < min_diff:
                    min_diff = abs(target - total)
                    min_sum = total
                    
                if total < target:                    
                    j += 1
                    
                elif total > target:
                    k -= 1
                    
                else:
                    j += 1
                    k -= 1
                    
        return min_sum
```