#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _search_pred(
            self, node: TreeNode, parents: List[TreeNode]
    ) -> Optional[TreeNode]:
        if node.left:
            parents.append(node)
            node = node.left
            while node.right:
                parents.append(node)
                node = node.right
            return node
        while parents:
            child = node
            node = parents.pop()
            if child is node.right:
                return node
        return None

    def _search_succ(
            self, node: TreeNode, parents: List[TreeNode]
    ) -> Optional[TreeNode]:
        if node.right:
            parents.append(node)
            node = node.right
            while node.left:
                parents.append(node)
                node = node.left
            return node
        while parents:
            child = node
            node = parents.pop()
            if child is node.left:
                return node
        return None

    def _search_first_ge(
            self, node: TreeNode, target: float, parents: List[TreeNode]
    ) -> Optional[TreeNode]:
        while node:
            if target < node.val:
                parents.append(node)
                node = node.left
            elif target > node.val:
                parents.append(node)
                node = node.right
            else:  # target == node.val
                return node
        node = parents.pop()
        if node.val < target:
            return self._search_succ(node, parents)
        else:
            return node

    def _search_last_node(
            self, node: TreeNode, parents: List[TreeNode]
    ) -> TreeNode:
        while node.right:
            parents.append(node)
            node = node.right
        return node

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []

        ub_parents = []
        ub_node = self._search_first_ge(root, target, ub_parents)
        if ub_node:
            lb_parents = ub_parents[:]
            lb_node = self._search_pred(ub_node, lb_parents)
        else:
            lb_parents = []
            lb_node = self._search_last_node(root, lb_parents)

        result = []
        for _ in range(k):
            closer_node = None
            closer_diff = float('inf')
            for node in (lb_node, ub_node):
                if node:
                    diff = abs(node.val - target)
                    if diff < closer_diff:
                        closer_node = node
                        closer_diff = diff
            result.append(closer_node.val)
            if closer_node is lb_node:
                lb_node = self._search_pred(lb_node, lb_parents)
            else:
                ub_node = self._search_succ(ub_node, ub_parents)
        return result
