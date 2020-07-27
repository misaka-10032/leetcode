# Missing Element in Sorted Array

https://leetcode.com/problems/missing-element-in-sorted-array/

## Brutal Force Solution

Intuitively, we can start with the brutal force solution. The goal is to find the k-th missing number, and we can easily
know the number of missing numbers between two existing numbers.

```
missing_cnt = a[i] - a[i-1] + 1
```

We keep aggregating `missing_cnt` until we find ourselves going overboard. Then we go back to `a[i-1]` and return
`a[i]-overboard`. One thing to take care is that the result could appear after the last element. In this case, we should
return `a[n-1]+delta`.

## Binary Search Solution

As the aggregated `missing_cnt` increases monotonically, we can do a binary search to find the k-th missing number. We
start by putting a pseudo `inf` at `a[n]` and initializing `(left, right) = (0, n)`. We keep reducing the range until
`left == right - 1`, which means we would have found where the k-th number lives.

There is a handy way to count the missing numbers between `(0, mid)`:

```
mid_missing_cnt = a[mid] - a[0] - mid
``` 

By comparing `mid_missing_cnt` with `k`, we can know if we want to search the left or the right region in the next step.

