# Continuous Subarray Sum

https://leetcode.com/problems/continuous-subarray-sum/

## Solution

The range sum query of an immutable array can be achieved with a prefix sum array. The problem of finding a range sum
being a multiple of `k` can be reduced to find the complement of a previous prefix sum. For example

```
k = 3

arr:  1,  1,  1,  1,  1, ...
              ^start      ^end
sum:  0,  1,  2,  3,  4,  5
                          ^end
comp: 0,  2,  1,  0,  2,  1
              ^start

* The start pointer is inclusive.
* The end pointer is exclusive.
```

We need to maintain a set of compliments. When a new prefix sum comes, we can just check if its complement is in the
complement set.

As the problem requires the sub-array to have at least two elements, we cannot add the current complement immediately to
the set before we move on to the next. Instead, we need to cache the previous sum, and add the complement of the
previous sum instead.

### Safe complement

The complement can be computed with `-v % k`. However, when `k == 0`, we need to return `v` it self.