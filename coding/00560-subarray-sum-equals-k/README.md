# Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/

## Solution

Prefix sum is used to answer range sum queries in an immutable array in `O(1)`.

```
sums[i] = sum(nums[:i+1])
```

As there are `O(n^2)` ranges to query. The naive solution has `O(n^2)` complexity. To optimize the problem, we can ask
ourselves the following question: **Fixing `i`, how many `j`s can give us the required sum?**

```
sum(nums[j:i+1]) == sums[i] - sums[j-1] == k
sums[j-1] == k - sums[i]
```

The problem is then reduced to finding the number of `j` (`j <= i`). This can be solved by maintaining a counter of all
the previous sums. We check the previous map and find the complements. After that, we update the map with the new sum,
and move on to the next element.