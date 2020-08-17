#!/usr/bin/env python3
# encoding: utf-8

import collections
import dataclasses
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclasses.dataclass
class PosNode:
    node: 'TreeNode'
    y: int
    x: int


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([PosNode(root, 0, 0)])
        x_to_y_to_vals = collections.defaultdict(
            lambda: collections.defaultdict(list))
        while queue:
            pos_node = queue.popleft()
            node, y, x = pos_node.node, pos_node.y, pos_node.x
            x_to_y_to_vals[x][y].append(node.val)
            if node.left:
                queue.append(PosNode(node.left, y+1, x-1))
            if node.right:
                queue.append(PosNode(node.right, y+1, x+1))
        result = []
        for x in sorted(x_to_y_to_vals.keys()):
            y_to_vals = x_to_y_to_vals[x]
            col = []
            for y in sorted(y_to_vals.keys()):
                col.extend(y_to_vals[y])
            result.append(col)
        return result
