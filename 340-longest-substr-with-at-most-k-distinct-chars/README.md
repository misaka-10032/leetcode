# Longest Substring with At Most K Distinct Characters

## Description

* Given a string, find the length of the longest substring `T` that
  contains at most k distinct characters.
* For example, Given s = `eceba` and k = 2,
  `T` is "ece" which its length is 3. 

## Solution

* Two pointer
  * `front` tries to get more distinct chars
  * `rear` shift one at a time
* Maintain a counter for the current window
* Boundary constraints: `front < n` and `rear < n`
* Edge case: `k = 0`
* Don't need to align `front` and `rear`.

