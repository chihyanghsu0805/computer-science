https://leetcode.com/problems/longest-increasing-subsequence/

```
class Solution:
    # Brute force is to build all sequence and check for increasinh, O(N*2^N)
    # Improving is to append to existing sequence if increasing, O(N^2)
    # Works if asked for the sequence
    # Optimal with binary search only works if finding length of sequence
    # Another solution is the longest common sequence with the sorted array    

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        seq = []
        
        for n in nums:
            
            if not seq or seq[-1] < n:
                seq.append(n)
                
            else:
                index = self.binary_search(seq, n)
                seq[index] = n
                
        return len(seq)
    
    def binary_search(self, arr, n):
        
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if arr[mid] < n:
                lo = mid + 1
                
            elif arr[mid] > n:
                hi = mid - 1
            
            # Special case when A[mid] == n
            # find the smallest index with values equal to n
            else:
                hi = mid - 1
                
        return lo
```

https://leetcode.com/problems/longest-common-subsequence/

```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Common technique for DP with two strings
        # Think of it as prepend " " to the string
        rows = len(text1) + 1
        cols = len(text2) + 1
        
        memo = [[0] * cols for _ in range(rows)]
        
        # Edge case with " " compared to text1
        for r in range(rows): 
            memo[r][0] = 1
        
        # Edge case with " " compared to text2
        for c in range(cols):
            memo[0][c] = 1
            
        for r in range(1, rows):
            for c in range(1, cols):
                
                if text1[r - 1] == text2[c - 1]:
                    memo[r][c] = 1 + memo[r - 1][c - 1]
                
                else:
                    memo[r][c] = max(memo[r - 1][c], memo[r][c - 1])
                    
        return memo[-1][-1] - 1 # Subtract the length of " " and " "
```

https://leetcode.com/problems/russian-doll-envelopes/

```

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        # Sort by ascending Width and the problem becomes 1D LongestIncreasingSequence
        # But choosing the minimum Height favors the next selection
        # So sort by descending height

        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        seq = []
        
        for w, h in envelopes:
            
            if not seq or (seq[-1][0] < w and seq[-1][1] < h):
                seq.append([w, h])
                
            else:
                index = self.binary_search(seq, h)
                seq[index] = [w, h]
                
        return len(seq)
    
    def binary_search(self, arr, h):
        
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if arr[mid][1] > h:
                hi = mid - 1
                
            elif arr[mid][1] < h:
                lo = mid + 1
                
            else:
                hi = mid - 1
                
        return lo
```