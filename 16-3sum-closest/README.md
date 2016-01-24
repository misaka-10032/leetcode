# Three sum closest

## Description

* [Link](https://leetcode.com/problems/3sum-closest/)
* Input: nums, type: list[int].
* Input: target, type: int.
* Ouput type: int. Closest sum of 3 to target.

## Solution

* Variant of [1-two-sum](../1-two-sum) and [15-3sum](../15-3sum).
* Trim state, because `nums[k] <= nums[i] <= nums[j]`.

```
if nums[k] * 3 > target + min_delta:
    break
```
