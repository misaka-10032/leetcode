# Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/

## Solution

A path consists of an up-path and a down-path. When we traverse the tree, we should use the return value to store the
longest up-path that includes the current node. In addition, we should track the global solution in an output argument.

```
def _find_longest_path(self, node: Optional[TreeNode], longest: List[int]) -> int:
    # Finds the longest path within the subtree of `node`. The return value
    # is the height of `node`. The longest path within the subtrees is tracked
    # in `longest`.
```

The length of the path the the number of nodes **minus one**.