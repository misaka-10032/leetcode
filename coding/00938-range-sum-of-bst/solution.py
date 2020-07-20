#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _find_next(self, node: TreeNode,
                   checkpoints: List[TreeNode]) -> Optional[TreeNode]:
        if node.right:
            node = node.right
            while node:
                checkpoints.append(node)
                node = node.left
            return checkpoints.pop()
        return checkpoints.pop() if checkpoints else None

    def _find_first_ge(self, root: TreeNode, lb: int,
                       checkpoints: List[TreeNode]) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val < lb:
                node = node.right
            elif node.val > lb:
                checkpoints.append(node)
                node = node.left
            else:
                return node
        return checkpoints.pop() if checkpoints else None

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        checkpoints = []
        node = self._find_first_ge(root, L, checkpoints)
        tot = 0
        while node and node.val <= R:
            tot += node.val
            node = self._find_next(node, checkpoints)
        return tot
