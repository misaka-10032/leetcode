# Three sum

## Description

* [Link](https://leetcode.com/problems/3sum/)
* Input: nums, type: list[int]. From which to find 3 int's.
* Output type: list[list[int]]. Each element is a 3-element list.

## Solution (dict)

* Sort (necessary here, unlike 2 sum).
* Map value to last index (this index matters if the list is sorted).


## Solution (search)

* Variant of [1-two-sum](../1-two-sum).
* Sort the list.
* Enumerate the first number, and find 2-sum on the right of it.
* Remember to eliminate same numbers of 2nd and 3rd when target get hit.
* Remember to eliminate the same numbers of 1st in whatever the case.