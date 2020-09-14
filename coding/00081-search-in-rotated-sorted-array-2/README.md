# Search in Rotated Sorted Array II

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

## Solution

This is the advanced problem of [the previous one](https://leetcode.com/problems/search-in-rotated-sorted-array/). The
previous problem restricts the numbers to be unique, so we can check if a sub-array contains a pivot by checking the
first and the last element.

However,  this problem allows the first and the last element to be equal. This could indicate two possible cases: 1) the
sub-array contains a single number, 2) the pivot appears in the sub-array. We cannot eliminate 1) unless we find a
different number within. To do this, we have to shrink the right boundary until a different number is found, or the
right boundary touches the left boundary.
