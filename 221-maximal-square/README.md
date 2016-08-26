# Maximal Square

* Easier version of [85](https://leetcode.com/problems/maximal-rectangle/)
* Having constraint that `h==w` reduces dependency.
* Let `f[i][j]` be max width if `a[i][j]` is taken as bottom-right corner.
* It requires `a[i][j]=='1'`, and depends on
  * `f[i-1][j-1]`
  * `f[i-1][j]`
  * `f[i][j-1]`
* The smallest of the three is the bottleneck hindering a larger square.
* Edge case: `f[-1][j] = f[i][-1] = 0`
* Optimization: only previous row is needed.