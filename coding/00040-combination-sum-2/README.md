# Combination Sum II

https://leetcode.com/problems/combination-sum-ii/

## Solution

Because each candidate can only appear once, we can search every combination, and back trace the valid combinations.

One thing to take care is that there could be duplicate candidates and the combination is required to be unique. For
example, in an array of 4 `1`'s, the combination of the first `1` and the second `1` should be considered as duplicate
as the combination of the third `1` and the fourth `1`. To resolve this, we can build a counter of the candidate array,
and iterate the possible counts.

As optimization, we can further keep track of the sum of all the element after the current element, i.e. to define
`sum[i]` to be the sum of `cand[i+1:]`. If we find the maximal gain does not reach our target, we can stop searching. To
have this optimization work well, we should also sort the candidates reversely. This way, if we are searching the branch
without picking the big numbers, we can save the searches in the small numbers.
