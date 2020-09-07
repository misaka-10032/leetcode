#!/usr/bin/env python3
# encoding: utf-8

from typing import Optional

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def _maybe_link_next(self, prev_node: Optional['Node'],
                         node: Optional['Node']) -> Optional['Node']:
        if not node:
            return prev_node
        if prev_node:
            prev_node.next = node
        return node

    def _find_first_child(self, node: 'Node') -> Optional['Node']:
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None

    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            it = head
            prev_child = None
            while it:
                prev_child = self._maybe_link_next(prev_child, it.left)
                prev_child = self._maybe_link_next(prev_child, it.right)
                it = it.next
            head = self._find_first_child(head)
        return root
