# Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Solution

First, we use `bisect_left()` to find the first element that is `>=` than the target value. If the target value is not
found, we return `[-1, 1]`.

Then, we use `bisect_right()` to find the first element that is `>` than the target value. The right boundary is one
element ahead of the found element.
