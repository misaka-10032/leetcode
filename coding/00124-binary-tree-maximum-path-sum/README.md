# Binary Tree Maximum Path Sum

https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Solution

A path consists of an up-path and a down-path. However, during recursion, the parent node only cares about the
children's up-path. Therefore, we could make the max up-path the return value, and keep track of the global max path in
an output argument.

```
def _max_path_sum(self, node: Optional[TreeNode], result: List[int]) -> int:
```
