# Maximum Sum of 3 Non-Overlapping Subarrays

https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

## Solution

The recurrence relation is clear in this problem. Let's define the max sum we can obtain at `nums[:end]` with `c`
sub-arrays as `f[c][end]`. Then we have the following.

```
f[c][end] = max([
    f[c][end-1],  # Do nothing with the last number.
    f[c-1][end-k] + sum(nums[end-k:end]),  # Include the last number in a subarray.
])
```

The initial value of the problem is `f[0][0] = 0`, as the sum of nothing is 0. We then iterate `c` and `end` to solve
all the involved problems.

The range sums can be pre-computed in `rsums`, so that `rsums[end] = sum(nums[end-k:end])`. The way to compute is
similar to the prefix sum, except that we subtract the number `nums[i-k]` that goes beyond the window.

As the problem asks for the indices for the sub-arrays, we need to track them properly as well. We can simply track the
last index of the solution at `f[c][end]`, so we can trace back all the indices.

```
new_sum = f[c-1][end-k] + sum(nums[end-k:end])
if f[c][end-1] < new_sum:
    last[c][end] = end - k
else:
    last[c][end] = last[c][end-1]
```

Back-tracing gives us the inverse indices.

```
inv = []
end = len(nums)
for c in range(3, -1, -1):
    start = last[c][end]
    inv.append(start)
    end = start
```
