# 24. Maximum Flow

## 24.1 Flow networks

Capacity c(u, v) >= 0

Flow f

0 <= f(u, v) <= c(u, v)

### Exercises

24.1-1
24.1-2
24.1-3
24.1-4
24.1-5
24.1-6
24.1-7

## 24.2 The Ford-Fulkerson method

Augmenting path p

$c_{f}$(p) = min{$c_{f}$(u, v) : (u, v) is in p}

$f_{p}$(u, v) = $c_{f}$(p), if (u, v) is on p

$f_{p}$(u, v) = 0, otherwise

Residual network $G_f$

$c_{f}$(u, v) = c(u, v) - f(u, v), if (u, v) $\in$ E

$c_{f}$(u, v) = f(v, u), if (v, u) $\in$ E

$c_{f}$(u, v) = 0, otherwise

Augmentation of flow

(ff')(u, v) = f(u, v) + f'(u, v) - f'(v, u), if (u, v) $\in$ E

(ff')(u, v) = 0, otherwise

```
Ford-Fulkerson-Method(G, s, t)
initialize flow f to 0
while p exists in G_f
    augment flow f along p
return f
```

$O(E|f^{*}|)$
```
Ford-Fulkerson(G, s, t)
for (u, v) in G.E
    (u, v).f = 0

while p from s to t in G_f
    c_f(p) = min(c_f(u, v) : (u, v) in p)
    for (u, v) in p
        if (u, v) in G.E
            (u, v).f = (u, v).f + c_f(p)
        else
            (u, v).f = (u, v).f - c_f(p)

return f
```

### Exercises
24.2-1
24.2-2
24.2-3
24.2-4
24.2-5
24.2-6
24.2-7
24.2-8
24.2-9
24.2-10
24.2-11
24.2-12
24.2-13

## 24.3 Maximum bipartite matching

A maximum matching is a matching of maximum cardinality

G' = (V', E')

E' = {(s, u) : u $\in$ L} $\cup$ {(u, v) : u $\in$ L, v $\in$ R, and (u, v) $\in$ E} $\cup$ {(v, t) : v $\in$ R}

M = {(u, v) : u $\in$ L, v $\in$ R, and f(u, v) > 0}

f(u, v) = 1 if (u, v) $\in$ M

f(u, v) = 0 if (u, v) $\notin$ M

Create flow network G', run Ford-Fulkerson on G', convert interge valued maximum into maximum matching for G

$O(VE)$

### Exercisese
24.3-1
24.3-2
24.3-3

## Problems
24-1
24-2
24-3
24-4
24-5
24-6
24-7
