#!/usr/bin/env python3
# encoding: utf-8


from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _traverse(self, node: Optional['TreeNode'], p: 'TreeNode', q: 'TreeNode',
                  lca: List['TreeNode']) -> Tuple[bool, bool]:
        if not node:
            return False, False
        if lca:
            return True, True
        left_has_p, left_has_q = self._traverse(node.left, p, q, lca)
        right_has_p, right_has_q = self._traverse(node.right, p, q, lca)
        has_p = left_has_p or right_has_p or node is p
        has_q = left_has_q or right_has_q or node is q
        if has_p and has_q:
            lca.append(node)
        return has_p, has_q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = []
        self._traverse(root, p, q, lca)
        return lca[0]
