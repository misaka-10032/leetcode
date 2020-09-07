# Word Break II

https://leetcode.com/problems/word-break-ii/

## Solution

Similar to the [previous](https://leetcode.com/problems/word-break/) problem, we use a recursive function `_search(i)`
to return the result. Instead of returning a bool, we return a list of valid sentences at `s[i:]`. We need to track the
possible decompositions after being searched to save future searches.
