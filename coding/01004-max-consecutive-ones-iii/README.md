# Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii/

## Solution

We use two pointers to find all possible windows. We start with `left = 0` and `right = -1`. Every time, we move
`right` forward for 1 step. In addition, we also track the `budget` remained. Every time we see a 0, we subtract 1 from
the budget, and do nothing if it's a 1. When we find our budget shows deficit, we start to move `left` forward until the
deficit goes out. At the end, we know it's the max window that ends at `right`, so we update the max counter.
