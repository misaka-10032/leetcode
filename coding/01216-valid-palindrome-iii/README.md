# Valid Palindrome III

https://leetcode.com/problems/valid-palindrome-iii/

## Solution

Dynamic programming. Use `f[left][right]` to track the minimal budget required to make a valid palindrome within
`s[left:right+1]`. We start with length 1, and then proceed. As we proceed, we have three candidates to choose from.

* `f[left+1][right-1]` if `s[left] == s[right]` and `left+1 <= right-1`.
* `f[left][right-1]` because we can remove `s[right]`.
* `f[left+1][right]` because we can remove `s[left]`.

To get the final result, we check if `f[0][n-1] <= k`.
 