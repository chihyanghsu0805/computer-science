https://leetcode.com/problems/jump-game/

```
class Solution:
    # A O(N^2) brute force solution would be allocate an array of boolean
    # And for each element iterate its jumps
    # And mark in the array as reachable (True)
    # O(N) greedy solution would be memoize maximum reachable
    # If the index is bigger than reachable, then it's not reachable
    # Order of comparison and memoization is important
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0
        
        for i, n in enumerate(nums):
            
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + n)
            
        return True
```

https://leetcode.com/problems/jump-game-ii/

```
class Solution:
    # For minimum jumps, it is straightforward to take the largest jump or Greedy
    # The problem is what if the largest jump does not reach the end
    # One way to think about it is all intermediate indices must be traveled
    # So if an index does not lead to the end, a smaller jump can be taken
    # And the invalid index will be included in the next jump
    # The difference between the largest jump and the smaller jump should be tracked

    def jump(self, nums: List[int]) -> int:
        
        min_jumps = 0        
        max_reach = 0
        # Use steps to track the difference between largest jump and smaller jump
        # steps are decremented for each iteration
        # when no more steps, a jump is needed
        # this jump can happen at any step
        steps = 0
        
        for i, n in enumerate(nums):
            
            if i == len(nums) - 1:
                return min_jumps
            
            max_reach = max(max_reach, i + n)
            
            # if not at start, decrement steps
            if i != 0:
                steps -= 1
            
            # if no more steps, increment jump and update steps
            if not steps:
                min_jumps += 1
                steps = max_reach - i
```