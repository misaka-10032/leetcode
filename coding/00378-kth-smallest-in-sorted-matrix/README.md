# Kth Smallest Element in a Sorted Matrix

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

## Solution

We can make educated guess of what `k`th element might be, and verify if it is really the `k`th element. The matrix has
a property that the min element is `matrix[0][0]` and the max element is `matrix[-1][-1]`. We can use tighten the bounds
and finally find the target element.

Given an educated guess of `target`, we can divide the matrix to the top-left part and the lower-right part, such that
the top-left part has value < `target`, and the bottom-right part has value >= `target`.

```
       +---
 < t   |
   +---+  >= t
 --+
```

To find the boundary, we start at the lower-left corner `(n, 0)`, and keep moving up and right. We keep moving up until
we see an element becomes < `target`. We keep moving right until we see an element becomes >= `target`. We keep track of
the count and the max value of the upper-left part when we move right. Notice that when we move right, if the current is
< `target`, the entire column above it is guaranteed to be < `target`. This property helps us track the count and the
max easily.

## Naive Solution

A matrix can be viewed as `m` rows. We can maintain a pointer for each row, and put the pointed value into a min heap.
Each time, we pop an element from the heap, and push its next element, if any.

The Time complexity of this solution is `O(k log n)`.
