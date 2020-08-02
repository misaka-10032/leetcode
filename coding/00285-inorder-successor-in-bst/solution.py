#!/usr/bin/env python3
# encoding: utf-8

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _find(self, root: 'TreeNode', v: int, checkpoints: List['TreeNode']) -> 'TreeNode':
        node = root
        while node:
            if v < node.val:
                checkpoints.append(node)
                node = node.left
            elif v > node.val:
                node = node.right
            else:  # v == node.val
                return node

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        else:
            checkpoints = []
            node = self._find(root, p.val, checkpoints)
            assert node is p
            return checkpoints[-1] if checkpoints else None
