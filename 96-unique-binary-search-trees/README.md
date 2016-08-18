# Unique Binary Search Trees

* Denote `G(n)` as number of unique BSTs with sequence `1..n`. 
* `F(n, i)` as number of unique BSTs with sequence `1..n`, rooted with `i`.

```
G(n) = F(n, 1) + F(n, 2) + ... + F(n, n)
```

* `F(n, i)` can be formulated into two sub-problems
 * `G(i-1)` with sequence `1 .. i-1`
 * `G(n-i)` with sequence `i+1 .. n`

```
G(n) = G(0)G(n-1) + ... + G(i)G(n-i-1) + ... + G(n-1)G(0)
```

* Define `G(0)=1` and bootstrap the recursion.
