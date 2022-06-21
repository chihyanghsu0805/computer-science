https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = float("inf")
        profit = 0
        
        for p in prices:
            
            if p < buy:
                buy = p
                
            profit = max(profit, p - buy)
            
        return profit
```

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = float("inf")
        profit = 0
        
        for p in prices:
            
            if p > buy:
                profit += (p - buy)
            
            buy = p
            
        return profit
```

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy1 = float("inf")
        buy2 = float("inf")
        
        profit1 = 0
        profit2 = 0
        
        for p in prices:
            buy1 = min(buy1, p)
            profit1 = max(profit1, p - buy1)
            buy2 = min(buy2, p - profit1)
            profit2 = max(profit2, p - buy2)
            
        return profit2    
```

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
```
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if 2* k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                profit += max(0, prices[i] - prices[i - 1])
            
            return profit
        
        memo = {}
        return self.max_profit(0, True, 0, k, prices, memo)
    
    def max_profit(self, start, buy, count, k, prices, memo):
        
        if (start, buy, count) in memo:
            return memo[(start, buy, count)]
        
        if start == len(prices):
            return 0
        
        if count >= k:
            return 0
        
        no_action = self.max_profit(start + 1, buy, count, k, prices, memo)
        if buy:
            memo[(start, buy, count)] = max(
                self.max_profit(start + 1, not buy, count, k, prices, memo) - prices[start],
                no_action
            )
            
        else:
            memo[(start, buy, count)] = max(
                self.max_profit(start + 1, not buy, count + 1, k, prices, memo) + prices[start],
                no_action
            )
        
        return memo[(start, buy, count)]
```

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        return self.max_profit(prices, 0, True, memo)
    
    def max_profit(self, prices, start, buy, memo):
        
        if (start, buy) in memo:
            return memo[(start, buy)]
        
        if start >= len(prices):
            return 0
        
        cooldown = self.max_profit(prices, start + 1, buy, memo)
        
        if buy:
            memo[(start, buy)] = max(
                cooldown,
                self.max_profit(prices, start + 1, not buy, memo) - prices[start]
            )
        
        else:
            memo[(start, buy)] = max(
                cooldown,
                self.max_profit(prices, start + 2, not buy, memo) + prices[start]
            )
            
        return memo[(start, buy)]
```