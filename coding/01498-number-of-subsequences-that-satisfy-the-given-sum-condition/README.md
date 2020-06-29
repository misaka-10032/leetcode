# Number of Subsequences That Satisfy the Given Sum Condition

## Description

Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less
or equal than target.

Since the answer may be too large, return it modulo `10^9 + 7`.

Example 1:

```
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
```

Example 3:

```
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
```

## Solution

It's easier to do min / max queries in a sorted array. In addition, the min / max values will not be changed in the
subsequences if the order changes. Therefore, let's sort the input array first.

To simplify the problem, let's first fix a number `v` to be the min, and probe the possible `u`s. Once we probed the
boundary of the `u`, the following two groups of indices become interesting:

```
S1 = {k | nums[k] == v}
S2 = {k | v + nums[k] <= target, and v < nums[k]}
```

At lease one value should appear in `S1`, because otherwise the min would change. There is no restriction on `S2`.
Therefore, the number of sequences with `v` being min is

```
((2 ** |S1|) - 1) * (2 ** |S2|)
```

### Binary Search

The right boundary of `S1` and `S2` can be found with binary search. As a convention, we use `[left, right)` to
represent a segment, with `left` being inclusive and `right` being exclusive. The problem is to find the right boundary.
For `S1`, it's the first element that is greater than `v`. For `S2`, it's the first element that is greater than
`target - v`. They are both **the first element that is GREATER than something**.

```python

def bin_search(nums, start, val):
    # Finds in nums[start:] the first element that is strictly greater val.
    # `start` is inclusive; `end` is exclusive. Returns the index of the
    # element. If not found, returns len(nums). Assumes `nums` is non-empty.
    end = len(nums)
    while start < end - 2:
        mid = (start + end) // 2
        mid_val = nums[mid]
        if mid_val <= val:
            start = mid + 1
        else:  # mid_val > val
            end = mid + 1

    for idx in range(start, end):
        if nums[idx] > val:
            return idx
    return end
```

The boundary conditions are tricky. The while loop can get trap when `nums[start:end]` has 0, 1, 2 elements. We should
get out of the trap, and do a brutal force check on the reduced candidates.

### Alternative

We could constrain `v` to be the max as well, but the situation becomes a bit more complicated. The following three
groups of indices are involved:

```
S1 = {k | v + nums[k] <= target, and v > nums[k]}
S2 = {k | v + nums[k] > target, and v > nums[k]}
S3 = {k | nums[k] == v}
```

At least one value should appear in `S3`, because otherwise the max would change. At least one value should appear in
`S1`, because otherwise the min would change. There is no restriction on `S2`. In addition, if `v` itself can be both
min and max, we should add the possible subsequences in `S3` as well. In summary, the number of subsequences with `v`
being max is

```
((2 ** |S1|) - 1) * (2 ** |S2|) * ((2 ** |S3|) - 1) +
1{v + v <= target} * ((2 ** |S3|) - 1)
```
