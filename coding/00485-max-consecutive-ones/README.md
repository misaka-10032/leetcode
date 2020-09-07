# Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

## Solution

We only need to scan the array once, and aggregate the counter at 1.

```
nums  1  1  0  1  1  1
cnt   1  2  0  1  2  3
max   1  2  2  2  2  3
```
