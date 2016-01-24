# Reverse integer

## Description

* [Link](https://leetcode.com/problems/reverse-integer/)
* Input: x, type: int
* Output: reverse, type: int

## Solution

* For a 32-bit integer:
 * TMIN = int(-(1 << 31))
 * TMAX = int((1 << 31) - 1)
* Python will automatically convert `int` to `long` when overflow happens, so just check if the number is within bound.
* -1 / 10 = -1, so do the while loop on positive numbers.