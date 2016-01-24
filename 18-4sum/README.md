# Four sum

## Description

* [Link](https://leetcode.com/problems/3sum/)
* Input: nums, type: list[int]. From which to find 4 int's.
* Output type: list[list[int]]. Each element is a -element list.

## Solution

* Variant of [15-3sum](../15-3sum).
* Lessons from the mistakes I've made:
 * Remember to eliminate the same numbers of 3rd and 4th when target is hit.
 * Remember to eliminate the same numbers of 1st and 2nd in whatever the case.
 * When eliminating same 1st's and 2nd's, place init at right place.
