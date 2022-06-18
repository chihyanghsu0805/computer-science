Monotonic stack is used to track indices of an array so the values are increasing / decreasing.

https://leetcode.com/problems/daily-temperatures/

```
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        warmer = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            
            current_temperature = temperatures[i]
            # Only keep temperatures higher than current, monotonic increasing
            # Because looking for the first date of warmer
            # Lower than current wont be needed
            while stack and temperatures[stack[-1]] <= current_temperature:
                stack.pop()
                
            if stack:
                warmer[i] = stack[-1] - i
                
            stack.append(i)
                
        return warmer        
```

https://leetcode.com/problems/largest-rectangle-in-histogram/

```
class Solution:
    # Brute force is O(N^2), computed all rectangle
    # Monotonic stack only computes the rectangle when previous is higher
    # Because the area is determined by the minimum height
    # So higher values are not needed for further comparisons

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        largest = 0
        
        for i, h in enumerate(heights + [0]): # [0] account for ascending array
            
            while stack and heights[stack[-1]] >= h:
                
                j = stack.pop()
                current_h = heights[j]
                if stack:
                    # [4, 5, 1]
                    # For the 5, width is 1
                    # For the 4, width is 2 
                    current_w = i - stack[-1] - 1
                else:
                    # Special case when h is smallest
                    # Previous ones are all popped
                    current_w = i
                    
                largest = max(largest, current_w * current_h)
                
            stack.append(i)
            
        return largest
```