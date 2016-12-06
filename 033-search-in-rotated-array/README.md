# Search in Rotated Sorted Array

* Find pivot first. It's `p` such that
  * `a[p] < a[r] < a[l]`
  * If `a[m] > a[l]`, then `m` is on the left, move `l` forward to `m+1`.
  * Else `m` is on the right, move `r` backward to `m`.
* Then find within range.
* Compare with [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/).
