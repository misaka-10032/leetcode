# Next Greater Element III

https://leetcode.com/problems/next-greater-element-iii/

## Solution

It's similar to [this problem](https://leetcode.com/problems/next-permutation/). We first convert the number to a list
of digits. Then, we do the following in order.

* Find the left boundary of a descending sequence on the right. Assign `p0` to its left.
* Find the last element `p` that is (strictly) greater the `p0` element.
* Swap `a[p0]` and `a[p]`.
* Revert `a[p0+1:]`.

```
9 7 4 8 7 6 5 2 1
    ^p0     ^p

9 7 5 8 7 6 4 2 1
    ^ swap  ^

9 7 5 1 2 4 5 7 8
      ^ reorder ^
```

There is a corner case with this problem. If the reordered number becomes greater than the max int32, we should return
-1. The max int32 is `(1 << 31) - 1`.
