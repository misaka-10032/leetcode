# Burst balloons

[Problem description](https://leetcode.com/problems/burst-balloons/)

Denote `scores[start][end]` as the best score achieved using balloons indexed from `start` to `end`. Initial states are

```
scores[i][i] = nums[i-1] * nums[i] * nums[i+1]
```

The transition function is

```
scores[start][end] = max_k {
  scores[start][k-1],
  scores[k+1][end],
  nums[k]*nums[start-1]*nums[end+1]
}
```

`k` is the index of the balloon to be burst in this round. `start..k-1` and `k+1..end` are now all burst. What's left is `start-1` and `end+1`. If they are out of bound, then they are assigned `1`.

Be careful of edge cases. Also, the test case contains an empty list... damn it :-(