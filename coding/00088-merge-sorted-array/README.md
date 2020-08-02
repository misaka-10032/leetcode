# Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

## Solution

It is apparent to use three pointers: `p1`, `p2`, `q` to track the position in the input `nums1`, `nums2`, and the
output array. It's asked to merge the arrays in-place within `nums1`. As it's told that `nums1` has enough space, we
don't need to worry about overwriting an unprocessed input.

The termination condition is tricky. We can have `p1` or `p2` terminate first, but in either case, we can stop when
`p2` terminates. If `p1` terminates first, we have to continue copying values from `p2` until `p2` terminates. If `p2`
terminates first, the rest of `p1` are sorted already, so we can return early. In either cases, we can use `p2 < 0` as
termination condition. Be careful that when `p1` terminates early, we need to generate a pseudo throwaway number to be
compared with the de-referenced `p2`.

