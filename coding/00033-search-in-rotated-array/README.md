# Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

## Solution

First, let's find the pivot with binary search. The middle point divides the array to two ranges.

* `a[left:mid]`
* `a[mid:right+1]`

The pivot can exist in either range. The one with a pivot would NOT be ascending, so let's try the right range first. If
`a[mid] > a[right]`, the pivot will exist in the right range.

Otherwise, it's tricky. The pivot can still be in the right range if it's smaller than it's left element. For example,

```
3 0 1
```

`a[mid]` (`0`) is not > `a[right]` (`1`), but itself is the pivot. We can tell this by comparing this `a[mid]` with
`a[mid-1]`. It becomes tricky again because we also need to check `mid > 1`.

Only then can we conclude that the pivot falls in the left range.

Once we find the pivot, we can narrow down the sub-array, and do a normal `bisect`.

## One-pass Solution

The target can be found in 1-pass as well. The idea is to test if the target falls in the range with pivot or the one
without. If it falls in the range without, we can stop the divide-and-conquer process and do a regular `bisect`.
Otherwise, we should narrow down the search space to the "pivot" range.

## Tip

Use `mid = (left + right + 1) // 2` will divide the array more evenly to the following ranges.

* `[left, mid)`
* `[mid, right]`

## Followup

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
