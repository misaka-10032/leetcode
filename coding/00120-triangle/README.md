# Triangle

* Let `f[i][j]` be min sum up till `i`th row and `j`th col.
* Each `(i, j)` can come from `(i-1, j)` or `(i-1, j-1)`.
* `f[i][j] = triangle[i][j] + min(f[i-1][j], f[i-1, j-1])`.
* Edge case
  * `f[i-1][-1] = f[i-1][i] = inf`
  * `f[-1][-1] = f[-1][0] = 0`
* Space compression
* Only previous row and current row is needed.
