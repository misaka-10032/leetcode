# Valid Palindrome II

https://leetcode.com/problems/valid-palindrome-ii/

## Solution

Match the `left` chars and the `right` chars **greedily**. Whenever a mismatch is found remove either the left char or
the right char and continue. Because we are only allowed to remove one char, we don't need recursion.