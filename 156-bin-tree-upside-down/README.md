# Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree `{1,2,3,4,5}`,

```
    1
   / \
  2   3
 / \
4   5
```

return the root of the binary tree `[4,5,2,#,#,3,1]`.

```
   4
  / \
 5   2
    / \
   3   1 
```

## Solution

```
  N               L
 / \    ---->    / \
L   R           R   N
```

* Rotate left, get `left_root` and `left_rightmost`
* Rotate right, get `right_root`
* `left_root` will be the new root
* Current root and `right_root` will be left/right children of `left_rightmost`
* Remember to reset left/right children of current root.
