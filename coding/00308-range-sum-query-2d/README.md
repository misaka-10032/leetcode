# Range Sum Query 2D - Mutable

https://leetcode.com/problems/range-sum-query-2d-mutable/

## Solution -- Segment Tree

A region can be divided into top-left, top-right, bottom-left, and bottom-right. We store redundant sums in the
sub-regions, and query the sums within the sub-regions.

## Solution -- Bit Indexed Tree

* Similar to 1d.
* For `bit[i][j]`
  * Denote `i`'s parent as `pi = i & -i`
    and `j`'s parent as `pj = j & -j`.
  * `bit[i][j]` represents range sum of `a[pi:i][pj:j]`.
  
```
a[:i][:j] = a[pi:i][pj:j] + a[ppi:pi][pj:j] + a[pi:i][ppj:pj] + a[:ppi][:ppj]
          = bit[i][j] + bit[pi][j] + bit[i][pi] + bit[ppi][ppj]
          = ...
```

* Each `bit[i][j]` corresponds to sum of a tile of numbers.

### Things to take care of

* Both `update` and `prefix` starts with `row+1` and `col+1`.
* `update` is to update it's siblings and uncles.
* `prefix` sum up the path to root.
* Maintain a separate `matrix` inside of the class, in order to compute difference in update.
