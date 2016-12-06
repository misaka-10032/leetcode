# Inorder Successor in BST

## Description

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

## Solution

* If `p` has right subtree, then the leftmost leaf of the
  right subtree would be the successor
* Otherwise, keep tracking to the parent, till who's left
  child of it's parent. That parent would be the successor.
