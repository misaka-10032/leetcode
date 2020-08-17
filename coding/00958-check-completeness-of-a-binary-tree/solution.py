#!/usr/bin/env python3
# encoding: utf-8

import collections
import dataclasses


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclasses.dataclass
class LayeredNode:
    node: 'TreeNode'
    index: int


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        # Traverse layer by layer, and count the number of nodes in each
        # layer. If we have a new layer to traverse, we check at the end
        # of the current layer of the number of nodes equals 2**h.
        queue = collections.deque([LayeredNode(root, 0)])
        prev_index = -1
        while queue:
            layered_node = queue.popleft()
            index = layered_node.index
            if index != prev_index+1:
                return False
            node = layered_node.node
            if node.right and not node.left:
                return False
            if node.left:
                queue.append(LayeredNode(node.left, index*2+1))
            if node.right:
                queue.append(LayeredNode(node.right, index*2+2))
            prev_index = index
        return True
