#!/usr/bin/env python3
# encoding: utf-8

"""This is not the solution for this problem.

Hypothetically, the interviewer can ask me to flatten the list in a layered
manner. It seems BFS, but would not require a queue for the optimal solution.
"""

from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def _find_last(self, node: 'Node') -> 'Node':
        while node.next:
            node = node.next
        return node

    def _find_first_with_child(self, node: 'Node') -> Optional['Node']:
        while node:
            if node.child:
                return node
            node = node.next
        return None

    def flatten(self, head: 'Node') -> 'Node':
        prev = head
        while True:
            node = self._find_last(head)
            prev = self._find_first_with_child(prev)
            if not prev:
                break
            node.next, prev.child.prev = prev.child, node
            prev.child = None
            prev = prev.next
            node = node.next
        return head
