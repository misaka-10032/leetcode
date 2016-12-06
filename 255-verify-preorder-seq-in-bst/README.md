# Verify Preorder Sequence in Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

## Solution

* Do it with stack can have guaranteed `O(n)`.
* Maintain a strict lower bound, and a decreasing (5, 4, 3...) stack.
* Trick is to discover the fact that the just popped element is
  __strict__ lower bound for the following elements. That's because
  the current element will be in the left subtree of those in the stack,
  and will be in the right subtree of the just popped element.

## Recursive Solution

* Times out; worst case is `O(n^2)`.