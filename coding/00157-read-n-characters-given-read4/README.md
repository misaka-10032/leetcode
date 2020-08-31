# Read N Characters Given Read4

https://leetcode.com/problems/read-n-characters-given-read4/

## Solution

Keep calling `read4()` until the rest of required chars `n` becomes zero. There are two corner cases to handle: 1) the
rest of `n` can be smaller than 4, so we only need to copy a part of the read chars. 2) The actually read chars can be
< 4 (short read). In this case, we should early return.

## Followup

https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
