https://leetcode.com/problems/search-in-rotated-sorted-array/

Binary search also works in rotated sorted array but needs more comparison.

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binary_search(nums, target)
    
    def binary_search(self, arr, n):
        
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if arr[mid] == n: # Special case when n is found
                return mid
            
            # This version of binary search only has one scenario when A[mid] == A[hi]
            # That is when len(A) == 1
            # Since A[mid] != n, n is not in A
            if arr[mid] == arr[hi]: 
                return -1

            # This version of binary search has two scenarios when A[mid] == A[lo]
            # len(A) == 2 and len(A) == 1
            # Since A[mid] == A[lo] != n, need to check A[hi]
                
            if arr[mid] == arr[lo]:
                lo = mid + 1
            
            # There are three scenarios for rotated sorted arrays with unique values
            # 1. No rotation, 12345
            # 2. infliction at left side, 51234
            # 3. infliction at right side, 34512

            elif arr[lo] < arr[mid]: # if left side is sorted
                
                if arr[lo] <= n < arr[mid]: # and the target falls in the left side
                    hi = mid - 1 # look in left side
                    
                else: 
                    lo = mid + 1 # look in right side
                    
            elif arr[mid] < arr[hi]: # if the right side is sorted
                
                if arr[mid] < n <= arr[hi]: # and the target falls in right side
                    lo = mid + 1 # look at right side
                
                else:
                    hi = mid - 1 # look at left side
                
        return -1        
```

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

```
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        return self.binary_search(nums, target)
    
    def binary_search(self, arr, n):
        
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if arr[mid] == n:
                return True
            
            # Special Case when A[mid] == A[hi] with duplicated values
            # Infliction may be between mid and hi, need to check every index in between
            if arr[mid] == arr[hi]:
                hi -= 1
            
            # Special Case when A[mid] == A[lo] with duplicated values
            # Infliction may be between mid and lo, need to check every index in between
            elif arr[mid] == arr[lo]:
                lo += 1
                
            else:
                
                if arr[lo] < arr[mid]:
                    
                    if arr[lo] <= n < arr[mid]:
                        hi = mid - 1
                        
                    else:
                        lo = mid + 1
                        
                elif arr[mid] < arr[hi]:
                    
                    if arr[mid] < n <= arr[hi]:
                        lo = mid + 1
                        
                    else:
                        hi = mid - 1
                        
        return False
```