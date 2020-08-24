# Lowest Common Ancestor of Deepest Leaves

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

## Solution

Traverse the tree. Return the height and the LCA in the meantime.

LCA should only be updated to the current node if the left and the right subtree have the same height. Otherwise, we
should inherit the LCA from the subtree with a greater height.
