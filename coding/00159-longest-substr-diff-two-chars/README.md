# Longest Substring with At Most Two Distinct Characters

## Description

* Given s = `eceba`, return `3`.
* Because `ece` is the longest that contains <=2 chars
  (`c` and `e`). 

## Solution

* Two pointers `l`, `r`.
* Try to move `r` forward as much as possible.
* Move `r` one more, and move `l` forward as less as possible.
* Think carefully about termination rule.

## Debug

* Made too much assumption about the state
* Didn't think of a termination rule of while loop
