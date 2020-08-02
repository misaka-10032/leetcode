# Consecutive Numbers Sum

https://leetcode.com/problems/consecutive-numbers-sum/

## Solution

```
N = n * a0 + (0 + 1 + ... + (n-1))
  = n * a0 + (n-1) * n // 2
```

where

```
n > 0
a0 > 0
```

We can start probing `n` already because the complexity is `O(sqrt(N))`. For each `n`, we compute a residue `r`.

```
r = N - (n-1) * n // 2
```

We keep probing `n` until `r <= 0`. A valid `n` will yield `r % n == 0`, so we maintain a counter for these valid `n`s.
