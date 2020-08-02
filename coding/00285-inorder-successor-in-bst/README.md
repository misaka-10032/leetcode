# Inorder Successor in BST

https://leetcode.com/problems/inorder-successor-in-bst/

## Facts

If `p` has right subtree, then the leftmost leaf of the right subtree would be the successor.

```
     p
      \
      x
     /
   ...
   /
  q
```


Otherwise, we have to keep tracking til the parent, and find one who is the left child of its parent. That parent would
be the successor.

```
   q
  /
 y
  \
  ...
    \
     x
      \
      p
```

## Solution 1

Case 1 is trivial. For case 2, we can first find `p` in the tree, and track the entire search path. We keep popping the
search path until we find a valid ascendant.

## Solution 2

For case 2, when we search `p` in the tree, we only save a checkpoint before going left. This makes the successor
searching easier: we simply pop an element in the checkpoints, if any.
