# Contains Duplicate III

## Balanced Tree

* Maintain a window size of `k+1` to be a binary search.
* For each window, query if `max - min > t`.
* Roll the window, remove the last one and insert the new one.
* As there's frequent insertion/deletion, we choose red black tree.

## Bucketing

* Divide all numbers into buckets,
  where bucket `b` takes `[tb, tb+b)`.
* If the newly inserted element falls into `b`,
  then `b-1`, `b`, `b+1` are all not allowed to be filled.
* Maintain a dict that maps bucket index `b` to the element in it.
* As bucket size is `t`, there could be at most one element in it.
* Remove/insert elements from `S` when rolling the window.
* Edge case `t=0` and `t<0`.
