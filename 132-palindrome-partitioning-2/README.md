# Palindrome Partitioning

## Divide and conquer with cache.

* `f[i, j]` denotes number of valid partitions within `[i, j)`.
* `p[i, j]` denotes if `s[i:i+j)` is palindrome.
* `p[i, j] = p[i+1, j-1] and s[i] == p[j-1]`
* Init `p[i, i+1] = p[i, i] = True`
* `f[i, j]`
  * If `p[i, j]` is not palindrome, `min_k( 1+f[i, k]+f[k, j] )`.
  * Otherwise, `0`.
* Use a set to store `(i, j)`, such that `p[i, j]` is true.
* Compute `f[i, j]` by divide and conquer, caching intermediate results.

## Dp

* The same for `p`
* Let `f[i]` be number of valid partitions within `[0, i)`
* `f[i] = min_{j: p[j, i] is True}( f[j] + 1 )`

## Save space

* `f[i]` only needs palindromes like `[k, i)`, maintain them in `prev`.
 * The new `k`s can be `k=i-1` and `k=i`.
 * They can also be those such that `s[k]==s[i-1]` and `k+1` is in `prev`.
