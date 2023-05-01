# 02. GettingStarted

## 2.1 Insertion Sort

```
Insertion-Sort(A, n)
for i = 2 to n
    key = A[i]
    j = i - 1
    while j > 0 and A[j] > key
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
```

Loop invariant:

1.  Initialization: It is tur prior to the first iteration of the loop
2.  Maintenance: If it is true before an iteration of the loop. it remains true before the next iteration
3.  Termination: The loop terminates, and when it terminates, the invariant - usually along with the reason that hte loop terminated - gives us a useful property that helps show that the algorithm is correct

### Exercises
-   2.1-1
-   2.1-2
-   2.1-3
-   2.1-4
-   2.1-5

## 2.2 Algorithms as a technology

### Exercises
-   2.2-1
-   2.2-2
-   2.2-3
-   2.2-4

## 2.3 Designing algorithms

Divide and Conquer
1. Divide
2. Conquer
3. Combine

```
Merge(A, p, q, r)
n_L = q - p + 1
n_R = r - q

for i = 0 to n_L - 1
    L[i] = A[p + i]

for j = 0 to n_R - 1
    R[j] = A[q + j + 1]

i = 0
j = 0
k = p

while i < n_L and j < n_R:
    if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
    else
        A[k] = R[j]
        j = j + 1
    k = k + 1

while i < n_L:
    A[k] = L[i]
    i = i + 1
    k = k + 1

while j < n_R:
    A[k] = R[j]
    j = j + 1
    k = k + 1

```

```
Merge-Sort(A, p, r)
if p >= r
    return

q = (p + r) // 2
Merge-Sort(A, p, q)
Merge-Sort(A, q + 1, r)
Merge-Sort(A, p, q, r)
```

### Exercises
-   2.3-1
-   2.3-2
-   2.3-3
-   2.3-4
-   2.3-5
-   2.3-6
-   2.3-7
-   2.3-8

## Problems

-   2-1
-   2-2
-   2-3
-   2-4
