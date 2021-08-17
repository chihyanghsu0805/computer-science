from __future__ import absolute_import, print_function

import numpy as np
import time
import argparse

run = 32 # tim_sort

def counting_sort(arr, exp=1):
  n = len(arr)
  output = [0]*n 
  count = [0]*10 # 0...9

  for i in range(n): 
    index = arr[i]//exp
    count[index%10] = count[index%10]+1 

  for i in range(1,10): 
    count[i] = count[i]+count[i-1] 

  i = n-1
  while i >= 0: 
    index = arr[i]//exp
    output[count[index%10]-1] = arr[i] 
    count[index%10] = count[index%10]-1
    i = i-1

  for i in range(n): 
    arr[i] = output[i] 

def radix_sort(arr):
  max_num = max(arr)
  exp = 1
  while max_num//exp > 0: 
    counting_sort(arr, exp) 
    exp = exp*10

def heapify(arr, n, i):
  largest = i
  lt = 2*i+1
  rt = 2*i+2

  if (lt < n) and (arr[i] < arr[lt]):
    largest = lt

  if (rt < n) and (arr[largest] < arr[rt]): 
    largest = rt

  if largest != i: 
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)

  for i in range(n-1, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

def merge(arr, lt_arr, rt_arr, start):
  i, j, k = 0, 0, start
     
  while (i < len(lt_arr)) and (j < len(rt_arr)):
    if lt_arr[i] < rt_arr[j]:
      arr[k] = lt_arr[i]
      i = i+1
    else:
      arr[k] = rt_arr[j]
      j = j+1
    k = k+1
  
  return i, j, k
              
def tim_sort(arr):
  n = len(arr)  
  for start in range(0, n, run):
    end = min(start+run, n)
    insertion_sort(arr, start, end)
        
  size = run
  while size < n:    
    for start in range(0, n, size*2):
      mid = min(n-1, start+size-1)
      end = min(n-1, mid+size)
      if mid < end:     
        lt_arr = arr[start:mid+1]
        rt_arr = arr[mid+1:end+1]
        i, j, k = merge(arr, lt_arr, rt_arr, start)

        while i < len(lt_arr):
          arr[k] = lt_arr[i]
          i = i+1
          k = k+1
              
        while j < len(rt_arr):
          arr[i] = rt_arr[j]
          j = j+1
          k = k+1   

    size = size*2
  
def partition(arr, low, high):
  i = low-1
  pivot = arr[high]

  for j in range(low, high):
    if arr[j] < pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1] 
  
  return i+1 

def quick_sort(arr, low=0, high=None):
  if high is None:
    high = len(arr)-1

  if low < high:
    pi = partition(arr, low, high)

    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi+1, high)

def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    l_arr = arr[:mid]
    r_arr = arr[mid:]

    merge_sort(l_arr)
    merge_sort(r_arr)

    merge(arr, l_arr, r_arr, 0)

def insertion_sort(arr, start=0, end=None):
  if end is None:
    end = len(arr)

  for i in range(start+1, end):
    key = arr[i]
    j = i-1

    while (j >= start) and (arr[j] > key): # find value smaller than key, can be replaced with binary search
      arr[j+1] = arr[j] 
      j = j-1

    arr[j+1] = key

def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    # Stable
    key = arr[min_idx] 
    while min_idx > i: 
      arr[min_idx] = arr[min_idx-1] 
      min_idx = min_idx-1

    arr[i] = arr[min_index]

def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--method", type=str, required=True)
  args = parser.parse_args()

  arr100 = np.random.randint(10000, size=100)
  tic100 = time.time()
  locals()[args.method](arr100)
  print(arr100)
  toc100 = time.time()-tic100

  print("N=100, Time:", toc100)

  arr10000 = np.random.randint(10000, size=10000)
  tic10000 = time.time()
  res = locals()[args.method](arr10000)
  toc10000 = time.time()-tic10000

  print("N=10000, Time:", toc10000)

