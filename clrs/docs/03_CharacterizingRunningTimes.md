# 03. 03_CharacterizingRunningTimes

## 3.1 $O$-notation, $\Omega$-notation, $\Theta$-notation

$O$-notation: upper bound, no faster than

$\Omega$-notation: lower bound, as least as fast than

$\Theta$-notation: tight bound

### Exercises
-   3.1-1
-   3.1-2
-   3.1-3

## 3.2 Asymptotic notation: formal definitions

O-notation: O(g(n)) = {$f(n)$: there exist positive constants $c$ and $n_0$ such that $ 0 <= f(n) <=
cg(n) $ for all $n >= n_0$}

$\Omega$-notation: O(g(n)) = {$f(n)$: there exist positive constants c and $n_0$ such that $ 0 <= cg(n) <= f(n) $ for all $n >= n_0$}

$\Theta$-notation: O(g(n)) = {$f(n)$: there exist positive constants c and n<sub>0</sub> such that $ 0 <= c_1g(n) <= f(n) <= c_2g(n) $ for all $n >= n_0$}

`Theorem 3.1`

For any two functions $f(n)$ and $g(n)$, we have $f(n)$ = $\Theta$ $(g(n))$ if and only if $f(n)$ = $O$ $(g(n))$ and $f(n)$ = $\Omega$ $(g(n))$

### Exercises
-   3.2-1
-   3.2-2
-   3.2-3
-   3.2-4
-   3.2-5
-   3.2-6
-   3.2-7

## 3.3 Standard notations and common functions

 Modular arithmetic
 -   If (a mod n) = (b mod n), we write a = b (mod n)

Functional iteration

The iterated logarithm function

### Exercises
-   3.3-1
-   3.3-2
-   3.3-3
-   3.3-4
-   3.3-5
-   3.3-6
-   3.3-7
-   3.3-8
-   3.3-9

## Problems

-   3-1
-   3-2
-   3-3
-   3-4
-   3-5
-   3-6
-   3-7
