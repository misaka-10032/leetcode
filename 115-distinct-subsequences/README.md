# Distinct Subsequences

* Let `f[i][j]` be number of occurrence of `t[:j]` in `s[:i]`.
* Having a new char in `s[i-1]`, we can choose to take it or not.
  * If we don't take it, then `f[i][j] = f[i-1][j]`.
  * If `s[i-1] == t[j-1]`, then we take it, `f[i][j] += f[i-1][j-1]`.
* Init
  * `f[i][0] = 1`.
* Assure that `len(s) >= len(t)`
