#!/usr/bin/env python3
# encoding: utf-8


import collections
from typing import Dict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs_traverse(self, root: TreeNode) -> Dict[int, TreeNode]:
        depth_to_rightmost_node_map = {}
        # The queue keeps track of the node and its depth as a tuple.
        # We only push nonnull nodes in this queue.
        queue = collections.deque()
        queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            depth_to_rightmost_node_map[depth] = node
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return depth_to_rightmost_node_map

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        depth_to_rightmost_node_map = self.bfs_traverse(root)
        max_depth = max(depth_to_rightmost_node_map.keys())
        return [depth_to_rightmost_node_map[d].val for d in range(1, max_depth + 1)]
