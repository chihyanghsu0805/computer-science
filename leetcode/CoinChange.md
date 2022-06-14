https://leetcode.com/problems/coin-change/

```
class Solution:
    
    # Unique coins, infinite use, minimum needed
    # Recursion Tree: change(amount) = min(
    #   change(amount - coins[0]),
    #   change(amount - coins[1]),
    #   ...)
    # Repetition when amount repeats --> memoization

    def coinChange(self, coins: List[int], amount: int) -> int:

        # Solution 1        
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0
        
        for a in range(amount + 1):
            for c in coins:
                if a >= c:
                    memo[a] = min(memo[a], memo[a - c] + 1)
        
        return memo[-1] if memo[-1] != float("inf") else -1

        # Solution 2
        memo = [float("inf")] * (amount + 1)
        memo[0] = 0        
        
        for c in coins:
            for a in range(c, amount + 1):
            
                memo[a] = min(memo[a], memo[a - c] + 1)
        
        return memo[-1] if memo[-1] != float("inf") else -1
```

https://leetcode.com/problems/coin-change-2/


```
class Solution:
    
    # Unique Coins, infinite use, number of combinations
    # Recursion Tree: Each branch is the coins
    #      1,2,5
    #    /   |   \
    #1,2,5  1,2,5 1,2,5
    # Repetition happens when sum is the same --> memoization

    def change(self, amount: int, coins: List[int]) -> int:
        
        # Solution 1: 2D DP
        rows = amount + 1 # 0 + [1:amount]
        cols = len(coins) + 1 # 0 + coins
        memo = [[0] * cols for _ in range(rows)]
        
        for c in range(cols): # Edge case when target is 0
            memo[0][c] = 1        
        
        for r in range(1, rows):
            for c in range(1, cols):
                
                memo[r][c] = memo[r][c - 1]
                
                if r >= coins[c - 1]:
                    memo[r][c] += memo[r - coins[c - 1]][c]
        
        return memo[-1][-1]

        # Solution 2: 1D DP
        # Use subset of coins and memoize combinations
        memo = [0] * (amount + 1)
        memo[0] = 1
        
        for c in coins:
            for r in range(amount + 1):
                
                if r >= c:
                    memo[r] += memo[r - c]
                    
        return memo[-1]
```