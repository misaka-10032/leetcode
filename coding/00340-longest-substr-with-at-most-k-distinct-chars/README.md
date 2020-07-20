# Longest Substring with At Most K Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## Description

* Given a string, find the length of the longest substring `T` that
  contains at most k distinct characters.
* For example, Given s = `eceba` and k = 2,
  `T` is "ece" which its length is 3. 

## Solution

* Two pointers
  * `end` tries to get one more char.
  * `start` shifts until the window is valid (i.e. contains at most k chars).
* Maintain a counter class for the current window, and remove the 0 counters timely.
* if `k == 0`, we can early return at the beginning.
