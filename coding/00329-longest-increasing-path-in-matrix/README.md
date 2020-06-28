# Longest Increasing Path in a Matrix

* `cache[i][j]` means the longest increasing path staring
  from `(i, j)`.
* If we have dfs `(i, j)`, it will be the same if we dfs
  it a second time.
* Strong constraint: strictly increasing
  * That indicates that we cannot go inversely
  * if `d1` leads to the longest remaining path,
    `d2, d3, d4` should all choose this direction.
  * `d1` won'd choose it again, because it's not increasing.
  * Past path won't appear in the future, because it's
    strictly increasing.
