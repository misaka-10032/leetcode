# Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

## Solution

We can pass in the previous node during recursion, so that we can reset its left pointer, and link its right pointer to
the current node.

Before recursion, we should cache the left and the right node, because they can change during recursion.

After recursion, we should return the last node, so the caller function can help us link the right (next) pointer. The
current node can either have or not have the left or the right node. For all the cases, we try to return `right_last`
first if any, otherwise `left_last` if any, and finally the current node.
