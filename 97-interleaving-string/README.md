# Interleaving String

* Let `f[i][j]` be whether it's possible to form `[0, i+j)` of
  `s3` by interleaving `[0, i)` of `s1` and `[0, j)` of `s2`.
* If `s3[i+j-1] == s1[i-1]`, `f[i][j] |= f[i-1][j]`.
* If `s3[i+j-1] == s2[j-1]`, `f[i][j] |= f[i][j-1]`.
* Init `f` with all False's.
* Edge case
  * `f[i][0] = s3[:i] == s1[:i]`
  * `f[0][j] = s3[:j] == s2[:j]`
