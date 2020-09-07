# Max Consecutive Ones II

https://leetcode.com/problems/max-consecutive-ones-ii/

## Solution

It adds complexity to [the previous problem](https://leetcode.com/problems/max-consecutive-ones/) by introducing
"previous gain". By flipping a zero, we can benefit from merging the previous chunk of 1's.

As this is an interview problem, the interviewer might challenge us to do it in 1-pass and with constant space. This is
doable, as long as we can track the previous gain properly.

When we see a 1, we increment `cnt` as usual. When we see a 0, we need to reset it as usual. However, before resetting
it, we need to update the `gain` to be 1 plus this `cnt`. The aggregated count so far is the updated `cnt` plus the
updated `gain`. And we always update the `max`. The underneath table is an example.

```
nums  0  1  0  1  1  0  0  1  1  1  1
cnt   0  1  0  1  2  0  0  1  2  3  4
gain  1  1  2  2  2  3  1  1  1  1  1
max   1  2  2  3  4  4  4  4  4  4  5
```
