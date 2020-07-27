# Vertical Order Traversal of a Binary Tree

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

## Solution

We traverse the tree and use `x_to_y_to_vals`, i.e. a default dict of default dict of list, to track the values. Be
aware that the question asks for

* Increasing order of `x`.
* Decreasing order of `y`.
* Sorted values of the same `(x, y)`.
