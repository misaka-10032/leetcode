#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _find_first(self, root: 'Node', checkpoints: List['Node']) -> 'Node':
        it = root
        while it.left:
            checkpoints.append(it)
            it = it.left
        return it

    def _find_next(self, node: 'Node', checkpoints: List['Node']) -> Optional['Node']:
        if node.right:
            node = node.right
            while node.left:
                checkpoints.append(node)
                node = node.left
            return node

        if not checkpoints:
            return None
        return checkpoints.pop()

    def _link_to_last(self, first: 'Node', checkpoints: List['Node']) -> 'Node':
        it = first
        while True:
            pre_it, it = it, self._find_next(it, checkpoints)
            if not it:
                break
            pre_it.right, it.left = it, pre_it
        return pre_it

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        checkpoints = []
        first = self._find_first(root, checkpoints)
        last = self._link_to_last(first, checkpoints)
        first.left, last.right = last, first
        return first
