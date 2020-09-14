# Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Solution

Similar to [this problem](https://leetcode.com/problems/search-in-rotated-sorted-array/). We do binary search to find
the pivot. The tricky corner case is that the `mid` element can be the pivot. In this case, both `[left, mid)` and
`[mid, right]` are ascending.
