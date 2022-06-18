https://leetcode.com/problems/permutation-in-string/

```
class Solution:
    # O(N^2 * S) brute force is nested for loops
    # Two optimization
    # 1. Use hashmap and counter variables (need/form) for comparing s1 to substring
    # 2. Sliding window for iterating s2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        char_counts = {}
        for ch in s1:
            char_counts[ch] = char_counts.get(ch, 0) + 1
        
        need = len(char_counts) # How many characters to compare
        form = 0 # How many in substring
            
        i = 0
        for j, ch in enumerate(s2): # Expand substring
            
            if ch in char_counts:
                char_counts[ch] -= 1
                if not char_counts[ch]: # All count of character is in substring
                    form += 1
                
            if j - i + 1 > len(s1): # Shrink till len(substring) == len(s1)
                
                ch_i = s2[i]                
                               
                if ch_i in char_counts:
                    
                    if not char_counts[ch_i]: # If all count of this character is used
                        form -= 1
                    
                    char_counts[ch_i] += 1
                    
                i += 1
                
            if form == need:
                return True
            
        return False
```

https://leetcode.com/problems/longest-substring-without-repeating-characters/
```
class Solution:
    # O(N^3) brute force is nested for loops for substring and check charcter in substring
    # Sliding window: expand till duplicatem shrink till no duplicate
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        memo = {}
        longest = 0
        
        i = 0
        for j, ch in enumerate(s):
            
            if ch in memo and memo[ch] >= i:
                i = memo[ch] + 1
            
            memo[ch] = j
            longest = max(longest, j - i + 1)
            
        return longest
```

https://leetcode.com/problems/minimum-window-substring/
```
class Solution:
    # Sliding window: expand till substring included, shrink till not included
    def minWindow(self, s: str, t: str) -> str:
        
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        
        count_s = {}
        
        need = len(count_t)
        form = 0
        
        min_win = float("inf")
        min_str = ""
        
        i = 0 
        for j, ch in enumerate(s):
            
            count_s[ch] = count_s.get(ch, 0) + 1
            
            if ch in count_t and count_t[ch] == count_s[ch]:
                form += 1
                
            while form == need:
                
                if j - i + 1 < min_win:
                    min_win = j - i + 1
                    min_str = s[i:j + 1]
                    
                ch_i = s[i]
                count_s[ch_i] -= 1
                
                if ch_i in count_t and count_t[ch_i] > count_s[ch_i]:
                    form -= 1
                    
                i += 1
                
        return min_str
    ```    
    